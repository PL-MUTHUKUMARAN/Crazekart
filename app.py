import uuid
import os
import secrets
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session, url_for, flash
from models import Order, db, User, Product, Cart, DeliveryDetails
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
from flask_migrate import Migrate


load_dotenv()

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db) 


with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    # Tells Flask-Login: use this function to load user from the db
    return db.session.get(User, int(user_id))


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))

        if not current_user.is_admin:
            flash("Admins only!")
            return redirect(url_for('index'))

        return f(*args, **kwargs)
    return wrapper


@app.route('/')
def home():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    products = Product.query.filter_by(isBest=True).all()
    return render_template('index.html', products=products)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        existing_user = User.query.filter(User.email == email).first()
        if existing_user:
            flash("Email already registered. Please login.")
            return redirect(url_for('login'))

        password = generate_password_hash(request.form.get('password'))


        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please login.")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        

        user = User.query.filter(User.email == email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password. Please try again.")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/admin_orders')
@login_required
@admin_required
def admin_orders():
    orders = Order.query.all()
    details = DeliveryDetails.query.all()
    return render_template('admin/adminOrders.html', items=orders, details=details)


@app.route('/add_product_details')
@login_required
@admin_required
def add_product_details():
    return render_template('addProduct.html')


@app.route('/add_product', methods=['POST'])
@login_required
@admin_required
def add_product():
    new_product = Product(
        name=request.form['name'],
        description=request.form['description'],
        price=request.form['price'],
        original_price=request.form['original_price'],
        discount=request.form['discount'],
        brand=request.form['brand'],
        category=request.form['category'],
        image=request.form['image'],
        color=request.form['color'],
        vcolor=request.form['vcolor'],
        rating=request.form['rating'],
        reviews=request.form['reviews'],
        isBest=request.form.get('isBest') == "True",
        colorVariety=request.form.get('colorVariety') == "True"
    )

    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for('product_category', category=request.form['category']))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/product_category/<string:category>')
def product_category(category):
    products = Product.query.filter_by(category=category).all()
    brands = list({p.brand for p in products})
    return render_template('productCategory.html', products=products, brands=brands, category=category)


@app.route('/buyingProductDetails/<int:id>')
def buyingProductDetails(id):
    product = Product.query.get(id)
    return render_template('buyingProductDetails.html', product=product)


@app.route('/remove_best_product/<int:id>')
@login_required
@admin_required
def remove_best_product(id):
    product = Product.query.get(id)

    if product:
        product.isBest = False
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete_product/<int:id>')
@login_required
@admin_required
def delete_product(id):
    product = Product.query.get(id)
    category = product.category

    if product:
        db.session.delete(product)
        db.session.commit()

    products = Product.query.filter_by(category=category).all()
    brands = list({p.brand for p in products})
    return render_template('productCategory.html', products=products, brands=brands)


@app.route('/edit_product/<int:id>')
@login_required
@admin_required
def edit_product_info(id):
    product = Product.query.get(id)
    return render_template('updateProduct.html', product=product)


@app.route('/update_product/<int:id>', methods=['POST'])
@login_required
@admin_required
def update_product(id):
    product = Product.query.get(id)

    if product:
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = request.form['price']
        product.original_price = request.form['original_price']
        product.discount = request.form['discount']
        product.brand = request.form['brand']
        product.category = request.form['category']
        product.image = request.form['image']
        product.color = request.form['color']
        product.vcolor = request.form['vcolor']
        product.rating = request.form['rating']
        product.reviews = request.form['reviews']
        product.isBest = True if request.form.get('isBest') == "True" else False
        product.colorVariety = True if request.form.get('colorVariety') == "True" else False

    db.session.commit()

    products = Product.query.filter_by(category=product.category).all()
    brands = list({p.brand for p in products})
    return render_template('productCategory.html', products=products, brands=brands)


@app.route('/mark_delivered/<order_id>', methods=['POST'])
@login_required
@admin_required
def mark_delivered(order_id):
    order_id = order_id.strip()

    order = Order.query.filter_by(order_id=order_id).first()
    order.payment_Status = "Paid"
    order.delivery_status = "Delivered"
    order.delivery_date = datetime.utcnow()
    db.session.commit()

    return redirect(url_for('admin_orders'))


@app.route('/addToCart/<int:id>', methods=['POST'])
@login_required
def addToCart(id):
    product = Product.query.get(id)
    color = request.form.get("color")
    image = request.form.get("image")

    item = Cart.query.filter_by(
        user_id=current_user.id,
        product_name=product.name,
        color=color
    ).first()

    if item:
        item.quantity += 1
    else:
        db.session.add(Cart(
            user_id=current_user.id,
            product_name=product.name,
            color=color,
            price=product.price,
            image=image,
            quantity=1
        ))

    db.session.commit()
    return redirect('/cart')


@app.route('/cart')
@login_required
def cart():
    items = Cart.query.filter_by(user_id=current_user.id).all()
    total = 0

    for item in items:
        total += item.price * item.quantity

    return render_template('cart.html', items=items, total=total)


@app.route('/update_qty/<int:id>/<string:action>')
@login_required
def update_qty(id, action):
    item = db.session.get(Cart, id)

    if action == "inc":
        item.quantity += 1
    elif action == "dec":
        item.quantity -= 1

    if item.quantity <= 0:
        db.session.delete(item)

    db.session.commit()
    return redirect('/cart')


@app.route('/remove/<int:id>')
@login_required
def remove(id):
    item = db.session.get(Cart, id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/cart')


@app.route('/buy_now/<int:id>', methods=['POST'])
@login_required
def buy_now(id):
    product = Product.query.get(id)
    color = request.form.get("color")
    image = request.form.get("image")
    session['buy_now'] = {
        'product_name': product.name,
        'price': product.price,
        'image': image,
        'color': color,
        'quantity': 1
    }
    return redirect('/checkOut')


@app.route('/checkOut')
@login_required
def checkOut():
    details = DeliveryDetails.query.filter_by(user_id=current_user.id).first()

    if details:
        return redirect('/orderSummary')

    return render_template('deliveryDetails.html')


@app.route('/edit_address')
@login_required
def edit_address():
    return render_template('deliveryDetails.html')


@app.route('/save_delivery_details', methods=['GET', 'POST'])
@login_required
def save_delivery_details():
    existing_details = DeliveryDetails.query.filter_by(user_id=current_user.id).first()

    if existing_details:
        existing_details.user_name = request.form['user_name']
        existing_details.email = request.form['email']
        existing_details.address = request.form['user_address']
        existing_details.pincode = request.form['pincode']
        existing_details.phoneNumber = request.form['phoneNumber']
    else:
        db.session.add(DeliveryDetails(
            user_id=current_user.id,
            user_name=request.form['user_name'],
            email=request.form['email'],
            address=request.form['user_address'],
            pincode=request.form['pincode'],
            phoneNumber=request.form['phoneNumber']
        ))

    db.session.commit()
    return redirect('/orderSummary')


@app.route('/orderSummary')
@login_required
def orderSummary():
    details = DeliveryDetails.query.filter_by(user_id=current_user.id).first()
    total = 0

    if 'buy_now' in session:
        item = session['buy_now']
        items = [item]
        total = item['price'] * item['quantity']
    else:
        card_items = Cart.query.filter_by(user_id=current_user.id).all()
        items = []
        for item in card_items:
            total += item.price * item.quantity
            items.append({
                'product_name': item.product_name,
                'price': item.price,
                'image': item.image,
                'color': item.color,
                'quantity': item.quantity
            })

    return render_template('orderSummary.html', details=details, items=items, total=total)


@app.route('/proceed_payment', methods=['POST', 'GET'])
@login_required
def proceed_payment():
    method = request.form.get('payment')
    if method == "cod":
        return redirect('/place_order_cod')
    return "hi"


@app.route('/place_order_cod')
@login_required
def place_order_cod():
    order_id = "ORD-" + str(uuid.uuid4())[:8]

    if 'buy_now' in session:
        item = session['buy_now']
        db.session.add(Order(
            user_id=current_user.id,
            product_name=item['product_name'],
            price=item['price'],
            image=item['image'],
            color=item['color'],
            quantity=item['quantity'],
            order_id=order_id,
            payment_method="COD",
            payment_Status="Pending"
        ))
        session.pop('buy_now')
        Cart.query.filter_by(
            user_id=current_user.id,
            product_name=item['product_name'],
            price=item['price'],
            image=item['image']
        ).delete()
    else:
        items = Cart.query.filter_by(user_id=current_user.id).all()

        for item in items:
            db.session.add(Order(
                user_id=current_user.id,
                product_name=item.product_name,
                price=item.price,
                image=item.image,
                color=item.color,
                quantity=item.quantity,
                order_id=order_id,
                payment_method="COD",
                payment_Status="Pending"
            ))
        Cart.query.filter_by(user_id=current_user.id).delete()

    db.session.commit()
    return render_template('orderSuccessful.html', order_id=order_id)


@app.route('/user_orders')
@login_required
def user_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('userOrders.html', items=orders)


if __name__ == '__main__':
    app.run(debug=True)

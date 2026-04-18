# 🛒 CrazeKart – Full-Stack E-Commerce Web Application

CrazeKart is a full-stack e-commerce web application built using **Flask (Python)**. It provides a complete online shopping experience including authentication, product management, cart system, and order processing.

🔗 **Live Website:** https://crazekart.onrender.com/index

---

## 🚀 Features

- 👤 User Registration & Login
- 🛍️ Product Browsing & Categories
- 🛒 Add to Cart / Remove from Cart
- 📦 Order Placement (COD)
- 📊 Admin Panel for Managing Products & Orders
- 📍 Delivery Address Management
- 🔐 Role-Based Access Control

---

## 🛠️ Tech Stack

**Backend:**

- Python (Flask)
- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate

**Frontend:**

- HTML
- CSS
- JavaScript

**Database:**

- PostgreSQL (Production - Render)
- SQLite (Local Development)

**Deployment:**

- Gunicorn
- Render

---

## ⚙️ Environment Variables

```env
DATABASE_URL=your_postgresql_database_url
SECRET_KEY=your_secret_key
```

---

## 📂 Project Structure

```
Crazekart/
Crazekart/
│── app.py
│── models.py
│── requirements.txt
│── Procfile
│
├── templates/
│   ├── *.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/PL-MUTHUKUMARAN/Crazekart.git
cd Crazekart
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment

Deployed on Render with PostgreSQL.

### Steps:

1. Push to GitHub
2. Create Web Service in Render
3. Add PostgreSQL database
4. Set environment variables
5. Deploy 🚀

---

## 🔐 Admin Setup

By default, all registered users are normal users.
To enable admin access, add this route in your `app.py`:

```python
@app.route('/make_admin/<email>')
def make_admin(email):
    user = User.query.filter_by(email=email).first()
    if user:
        user.is_admin = True
        db.session.commit()
        return "User is now admin"
    return "User not found"
```

### Usage

1. Register a user
2. Login
3. Open browser and run:

```
https://crazekart.onrender.com/make_admin/your_email@example.com
```

Now that user will have admin privileges.

---

## ⚠️ Notes

- PostgreSQL is used in production
- SQLite is used for local testing
- Use Flask-Migrate for database changes

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**MUTHUKUMARAN P**

- GitHub: https://github.com/PL-MUTHUKUMARAN

---

## 🔗 Connect with Me

- 💼 LinkedIn: https://www.linkedin.com/in/plmuthukumaran/

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

from app import app
from models import db, Product

with app.app_context():

    # Guard prevents duplicate products if you run this file twice
    if Product.query.first() is not None:
        print("Products already exist in DB. Skipping seed to avoid duplicates.")
        exit()

    products = [

        # ================= AIRPODS =================
        {
            "name": "boAt Airdopes 111 – 28 Hrs, 13mm Drivers, ASAP Charge",
            "description": "boAt Airdopes 111 wireless earbuds with 28 hours total playback, 13mm drivers, and ASAP charge technology for fast charging.",
            "price": 1118,
            "original_price": 1599,
            "discount": 30,
            "brand": "boAt",
            "category": "airpodes",
            "image": "airpodes/boAtAirdopes111_",
            "color": "Sand Peari",
            "vcolor": "Carbon Black",
            "rating": 4.2,
            "reviews": 5432,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "boAt Airdopes 411 ANC – ANC, 17.5 Hrs, ENx Mic",
            "description": "boAt Airdopes 411 ANC wireless earbuds with Active Noise Cancellation, 17.5 hours playback, and ENx mic for clear calls.",
            "price": 2499,
            "original_price": 5999,
            "discount": 58,
            "brand": "boAt",
            "category": "airpodes",
            "image": "airpodes/boAtAirdopes411ANC",
            "color": "Black",
            "vcolor": "Blue",
            "rating": 4.0,
            "reviews": 23456,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "boAt Airdopes 511 V2 – 30 Hrs, 6mm Drivers, IPX4",
            "description": "boAt Airdopes 511 V2 wireless earbuds with 30 hours playback, 6mm dynamic drivers, and IPX4 water resistance.",
            "price": 1999,
            "original_price": 3999,
            "discount": 50,
            "brand": "boAt",
            "category": "airpodes",
            "image": "airpodes/boAtAirdopes511V2_",
            "color": "Black",
            "vcolor": "Furious Blue",
            "rating": 4.0,
            "reviews": 12345,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "Noise Buds N1 Pro",
            "description": "Noise Buds N1 Pro wireless earbuds with Active Noise Cancellation up to 30dB and up to 60 hours of playback.",
            "price": 1399,
            "original_price": 4999,
            "discount": 72,
            "brand": "Noise",
            "category": "airpodes",
            "image": "airpodes/NoiseBudsN1Pro",
            "color": "Green",
            "vcolor": "Beige",
            "rating": 3.8,
            "reviews": 8765,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "OnePlus Nord Buds 3 Pro",
            "description": "OnePlus Nord Buds 3 Pro with up to 49dB noise cancellation and fast charging that gives 11 hours playback in just 10 minutes.",
            "price": 2599,
            "original_price": 3699,
            "discount": 30,
            "brand": "Oneplus",
            "category": "airpodes",
            "image": "airpodes/oneplus",
            "color": "Black",
            "vcolor": "White",
            "rating": 4.2,
            "reviews": 3210,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "Boult GOBOULT",
            "description": "Boult GOBOULT wireless earbuds with 48 hours playback, built-in app support, and ultra-low 45ms latency for gaming.",
            "price": 1208,
            "original_price": 3499,
            "discount": 65,
            "brand": "Boult",
            "category": "airpodes",
            "image": "airpodes/boult",
            "color": "Black",
            "vcolor": "White",
            "rating": 4.1,
            "reviews": 1987,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "boAt Airdopes Alpha",
            "description": "boAt Airdopes Alpha wireless earbuds with 35 hours playback, 13mm drivers, and ENx microphones for crystal clear calls.",
            "price": 899,
            "original_price": 3490,
            "discount": 74,
            "brand": "boAt",
            "category": "airpodes",
            "image": "airpodes/boAtAirdopesAlpha",
            "color": "Black",
            "vcolor": "White",
            "rating": 4.5,
            "reviews": 4567,
            "isBest": True,
            "colorVariety": True
        },
        {
            "name": "realme Buds T200x",
            "description": "realme Buds T200x with quad microphones, 45ms low latency, and up to 48 hours playback with fast charging support.",
            "price": 1599,
            "original_price": 2499,
            "discount": 36,
            "brand": "Realme",
            "category": "airpodes",
            "image": "airpodes/realme",
            "color": "Black",
            "vcolor": "White",
            "rating": 4.0,
            "reviews": 2345,
            "isBest": False,
            "colorVariety": True
        },

        # ================= HEADPHONES =================
        {
            "name": "boAt Rockerz 450 Batman DC Edition",
            "description": "boAt Rockerz 450 Batman Edition Bluetooth headphones with 40mm drivers, up to 20 hours playback, and voice assistant support.",
            "price": 1799,
            "original_price": 3990,
            "discount": 55,
            "brand": "boAt",
            "category": "earphones",
            "image": "earphones/boAt Rockerz",
            "color": "Black",
            "rating": 4.8,
            "reviews": 8000,
            "isBest": True,
            "colorVariety": False
        },
        {
            "name": "boAt Rockerz 450",
            "description": "boAt Rockerz 450 over-ear Bluetooth headphones with 15 hours playback, adaptive headband, and immersive audio experience.",
            "price": 1699,
            "original_price": 3990,
            "discount": 57,
            "brand": "boAt",
            "category": "earphones",
            "image": "earphones/boAt TRebel Rockerz 450 ",
            "color": "Beige",
            "vcolor": "Luscious Black",
            "rating": 4.8,
            "reviews": 2999,
            "isBest": False,
            "colorVariety": True
        },

        # ================= TV =================
        {
            "name": "Toshiba 55 inch 4K Ultra HD Smart TV",
            "description": "Toshiba 55 inch Z570RP Series 4K Ultra HD Smart QLED TV with Dolby Vision, smart features, and immersive sound.",
            "price": 38999,
            "original_price": 71999,
            "discount": 46,
            "brand": "Toshiba",
            "category": "tv",
            "image": "TV/toshiba",
            "rating": 4.3,
            "reviews": 2000,
            "isBest": False,
            "colorVariety": False
        },
        {
            "name": "Sony 55 inch BRAVIA Smart TV",
            "description": "Sony BRAVIA 55 inch 4K Ultra HD Smart LED Google TV with powerful processor, vibrant display, and smart connectivity.",
            "price": 55990,
            "original_price": 99900,
            "discount": 44,
            "brand": "Sony",
            "category": "tv",
            "image": "TV/sony",
            "rating": 4.7,
            "reviews": 20000,
            "isBest": False,
            "colorVariety": False
        },

        # ================= WATCHES =================
        {
            "name": "Giordano Designer Watch",
            "description": "Giordano multifunction designer watch with square dial, premium leather strap, suitable for casual and formal wear.",
            "price": 5299,
            "original_price": 7950,
            "discount": 33,
            "brand": "Giordano Designer",
            "category": "watches",
            "image": "watches/Giordano",
            "color": "Black",
            "vcolor": "Rose Gold",
            "rating": 4.0,
            "reviews": 3000,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "Daniel Hechter Watch",
            "description": "Daniel Hechter Paris multifunction watch with octagonal dial, stylish design, and durable silicon strap.",
            "price": 3799,
            "original_price": 6450,
            "discount": 41,
            "brand": "Daniel Hechter",
            "category": "watches",
            "image": "watches/Daniel Hechter",
            "color": "Green",
            "vcolor": "Black",
            "rating": 3.9,
            "reviews": 5000,
            "isBest": True,
            "colorVariety": True
        },

        # ================= SPEAKERS =================
        {
            "name": "Boat Nirvana Luxe Speaker",
            "description": "Boat Nirvana Luxe 100W Bluetooth speaker with 360° surround sound, spatial audio, NFC pairing, and 15 hours battery.",
            "price": 8990,
            "original_price": 24990,
            "discount": 64,
            "brand": "boAt",
            "category": "speakers",
            "image": "speakers/boat",
            "color": "Charcoal Black",
            "vcolor": "Ivory White",
            "rating": 3.8,
            "reviews": 3000,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "Marshall Woburn III Speaker",
            "description": "Marshall Woburn III home speaker with HDMI input, Bluetooth 5.2, and premium high-fidelity audio output.",
            "price": 54999,
            "original_price": 59999,
            "discount": 8,
            "brand": "Marshall",
            "category": "speakers",
            "image": "speakers/marshall",
            "color": "Black",
            "vcolor": "Brown",
            "rating": 4.6,
            "reviews": 5000,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "Boat Stone 1450",
            "description": "Boat Stone 1450, 20W, IPX7 Waterproof, 12hrs Playtime, Bluetooth Speaker, Wireless Speaker, Portable Speaker (Charcoal Black)",
            "price": 4999,
            "original_price": 8990,
            "discount": 51,
            "brand": "boAt",
            "category": "speakers",
            "image": "speakers/boAt Stone 1450 ",
            "color": "Blue",
            "vcolor": "Black",
            "rating": 4.2,
            "reviews": 2000,
            "isBest": False,
            "colorVariety": True
        },

        # ================= MOBILES =================
        {
            "name": "vivo X300 Pro 5G",
            "description": "vivo X300 Pro 5G smartphone with 8GB RAM, 256GB storage, premium design, and advanced camera features.",
            "price": 109998,
            "original_price": 119999,
            "discount": 8,
            "brand": "Vivo",
            "category": "mobile",
            "image": "mobile/vivo",
            "color": "Elite Black",
            "vcolor": "Dune Gold",
            "rating": 4.5,
            "reviews": 5000,
            "isBest": True,
            "colorVariety": True
        },
        {
            "name": "OnePlus 15",
            "description": "OnePlus 15 flagship smartphone with Snapdragon 8 Elite processor, 16GB RAM, 512GB storage, and 165Hz display.",
            "price": 79999,
            "original_price": 83999,
            "discount": 5,
            "brand": "Oneplus",
            "category": "mobile",
            "image": "mobile/oneplus",
            "color": "Sand Storm",
            "vcolor": "Infinite Black",
            "rating": 4.6,
            "reviews": 5000,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "Samsung Galaxy S25 Ultra",
            "description": "Samsung Galaxy S25 Ultra with powerful performance, premium design, and advanced AI camera features.",
            "price": 109999,
            "original_price": 129999,
            "discount": 16,
            "brand": "Samsung",
            "category": "mobile",
            "image": "mobile/samsung",
            "color": "Titanium Silverblue",
            "vcolor": "Titanium Black",
            "rating": 4.3,
            "reviews": 5000,
            "isBest": False,
            "colorVariety": True
        },
        {
            "name": "iPhone 17 Pro Max",
            "description": "Apple iPhone 17 Pro Max with A19 Pro chip, ProMotion display, and industry-leading camera system.",
            "price": 219900,
            "original_price": 229900,
            "discount": 6,
            "brand": "Apple",
            "category": "mobile",
            "image": "mobile/apple",
            "color": "Titanium Silverblue",
            "vcolor": "Deep Blue",
            "rating": 4.5,
            "reviews": 5000,
            "isBest": False,
            "colorVariety": True
        }
    ]

    for p in products:
        db.session.add(Product(**p))

    db.session.commit()
    print("Products seeded successfully!")

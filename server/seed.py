#!/usr/bin/env python3

from app import app
from models import db, Hotel, Customer, Review

with app.app_context():
    
    Hotel.query.delete()
    Customer.query.delete()
    Review.query.delete()

    hotels = []
    hotels.append(Hotel(name="Marriott"))
    hotels.append(Hotel(name="Holiday Inn"))
    hotels.append(Hotel(name="Hampton Inn"))

    customers = []
    customers.append(Customer(first_name="Alice", last_name="Baker"))
    customers.append(Customer(first_name="Barry", last_name="Smith"))
    customers.append(Customer(first_name="Chris", last_name="Jones"))

    reviews = []
    reviews.append(Review(hotel_id=1, customer_id=1, rating=5))
    reviews.append(Review(hotel_id=2, customer_id=1, rating=5))
    reviews.append(Review(hotel_id=1, customer_id=2, rating=4))
    reviews.append(Review(hotel_id=1, customer_id=1, rating=3))

    db.session.add_all(hotels)
    db.session.add_all(customers)
    db.session.add_all(reviews)
    db.session.commit()
    print("🌱 Hotels, Customers, and Reviews successfully seeded! 🌱")

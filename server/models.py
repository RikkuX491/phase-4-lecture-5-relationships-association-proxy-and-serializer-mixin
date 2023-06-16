from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hotel(db.Model, SerializerMixin):
    __tablename__ = 'hotels' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 5:
            raise ValueError(f"{key} must be at least 5 characters long.")
        return value
    
    def __repr__(self):
        return f"Hotel # {self.id}: {self.name} hotel"

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'    

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    __table_args__ = (
        db.CheckConstraint('(first_name != last_name)'),
    )

    @validates('first_name', 'last_name')
    def validate_first_name(self, key, value):
        if value is None:
            raise ValueError(f"{key} cannot be null.")
        elif len(value) < 4:
            raise ValueError(f"{key} must be at least 4 characters long.")
        return value
    
    def __repr__(self):
        return f"Customer # {self.id}: {self.first_name} {self.last_name}"
    
class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f"Review # {self.id}: {self.customer.first_name} {self.customer.last_name} left of a review for {self.hotel.name} with a rating of {self.rating}."
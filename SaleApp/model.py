import json
from symtable import Class

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from SaleApp import app, db
from enum import Enum as RoleEnum

class UserRole(RoleEnum):
    USER =1
    ADMIN=2


class base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique= True)
    def __str__(self):
        return self.name

class User(base):
    username = Column(String(100),nullable=False)
    password = Column(String(50), nullable=False, unique=True)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.USER)
    avatar = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1740037805/apple-iphone-16-pro-natural-titanium_lcnlu2.webp")


class Category (base):
    products=relationship('Product', backref='category', lazy=True)


class Product (base):
    price = Column(Float, default=0.0)
    image = Column(String(300),default="https://res.cloudinary.com/dy1unykph/image/upload/v1740037805/apple-iphone-16-pro-natural-titanium_lcnlu2.webp")
    cate_id = Column(Integer,ForeignKey(Category.id), nullable=False)



if __name__=="__main__":
    with app.app_context():
        db.create_all()

        # c1 = Category(name="Mobile")
        # c2 = Category(name="Laptop")
        # c3 = Category(name="Tablet")
        # db.session.add_all([c1, c2, c3])
        #
        # with open("SaleApp/data/products.json", encoding="utf-8") as f:
        #     prods=json.load(f)
        #     for p in prods:
        #         db.session.add(Product(**p))

        u =User(username='user', password='123', name='User')
        db.session.add(u)
        db.session.commit()



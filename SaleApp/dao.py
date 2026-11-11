import json

from flask.globals import app_ctx

from model import Product, User, db, app
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash



def add_user(name, username, password, avatar):
    password = hashlib.md5()
    u = User(name=name, username=username, password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()
    def __str__(self):
        return u.name

def auth_user(name, password):
    password=hashlib.md5()
    u1 = User.query.filter(User.username.__eq__(name), User.password.__eq__(password))



def load_categories():
    with open("data/cates.json", encoding="utf-8") as f:
        return json.load(f)


def load_products(q=None, cate_id=None):
    with open("data/products.json", encoding="utf-8") as f:
        prods = json.load(f)

        if q:
            prods = [p for p in prods if p["name"].find(q)>=0]

        if cate_id:
            prods = [p for p in prods if p["cate_id"].__eq__(int(cate_id))]

        return prods

def get_product_by_id(id):
    # with open("data/products.json", encoding="utf-8") as f:
    #     prods = json.load(f)
    #     for p in prods:
    #         if p["id"]==id:
    #             return p
    return  Product.query.get(id)

if __name__=="__main__":
    with app.app_context():
        print(add_user('user1', 'mickey', '1234','https://res.cloudinary.com/dy1unykph/image/upload/v1740037805/apple-iphone-16-pro-natural-titanium_lcnlu2.webp' ))
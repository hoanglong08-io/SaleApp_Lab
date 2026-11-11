from flask import Flask, render_template, request, session, flash
from werkzeug.utils import redirect

import dao
from SaleApp import app

app.secret_key="1234"

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    return render_template("index.html", prods=dao.load_products(q=q, cate_id=cate_id))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method.__eq__('POST'):
        user=request.form.get("username")
        pss=request.form.get("pswd")
        er_m = None
        session['username'] = user
        session['password'] = pss

        if user == 'admin' and pss == '123':
            return redirect('/')
        else:
            er_m = "Tai khoan dang nhap khong chinh xac"
            return render_template("login.html", er_m=er_m)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/product/<int:id>")
def details(id):
    return render_template("prod_detail.html", prod=dao.get_product_by_id(id))

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }


if __name__=="__main__":
    app.run(debug=True)
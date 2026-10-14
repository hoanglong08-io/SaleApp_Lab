

from flask import Flask, render_template, request
import dao


app = Flask(__name__)
@app.route("/")
def index ():
    q = request.args.get('q')
    cate_id = request.args.get('cate_id')
    cates = dao.load_cates()
    prods = dao.load_products(q,cate_id)

    return render_template("index.html", cates=cates, prods = prods)


@app.route("/product/<int:id>")
def detail(id):
    return render_template("prod_detail.html", id=id)

# @app.route("/?cate_id=<int: id>")
# def cate(id):
#     cates = dao.
#     tab = ((cate for cate in cates if cate['id'] == id))



if __name__ == "__main__":
    app.run(debug=True)
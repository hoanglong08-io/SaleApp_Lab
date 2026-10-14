import json

def load_cates():
    with open("Data/cate.json", encoding="utf-8") as f:
        return json.load(f)

def load_products(q=None, cate_id=None):
    with open("Data/product.json", encoding="utf-8") as f:
        prods = json.load(f)

        if q:
            prods = [p for p in prods if p['name'].find(q) >= 0]

        if cate_id:
            prods = [p for p in prods if p['cate_id'].__eq__(int(cate_id))]

        return prods

if __name__ == "__main__":
    print(load_products())

from flask import Flask, request, abort

app = Flask(__name__)
products = {}
last_id = 0

@app.post("/product")
def add_product():
    if ("name" not in request.json) or ("description" not in request.json):
        abort(400)
    global last_id
    products[last_id] = {
        "id": last_id,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    last_id += 1
    print(products)
    return products[last_id - 1]

@app.get("/product/<int:product_id>")
def get_product(product_id):
    if product_id not in products:
        abort(400)
    return products[product_id]

@app.put("/product/<int:product_id>")
def update_product(product_id):
    if product_id not in products:
        abort(400)
    if "name" in request.json:
        products[product_id]["name"] = request.json["name"]
    if "description" in request.json:
        products[product_id]["description"] = request.json["description"]
    return products[product_id]

@app.delete("/product/<int:product_id>")
def delete_product(product_id):
    if product_id not in products:
        abort(400)
    pr = products[product_id]
    products.pop(product_id)
    return pr

@app.get("/products")
def get_products():
    return list(products.values())

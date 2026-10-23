from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to Flatiron Products"

@app.route("/products")
def get_products():
    return jsonify(products), 200

@app.route("/products/<int:id>")
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)

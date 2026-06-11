from flask import Flask, jsonify, render_template

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Arroz", "precio": 4.50},
    {"id": 2, "nombre": "Azúcar", "precio": 3.80},
    {"id": 3, "nombre": "Aceite", "precio": 9.50}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/productos")
def get_productos():
    return jsonify(productos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

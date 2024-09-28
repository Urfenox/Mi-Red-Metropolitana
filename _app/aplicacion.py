from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    contexto = {
        "tipo": "Bip!",
        "saldo": "3.000",
        "tarjeta": "123456789",
        "lineas": ["l1", "l2", "l3"],
        "micros": [],
    }
    return render_template('index.html', **contexto)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

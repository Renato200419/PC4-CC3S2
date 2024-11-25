from flask import Flask
from product_catalog.src.controllers import product_blueprint

app = Flask(__name__)

# Registrar las rutas del controlador
app.register_blueprint(product_blueprint, url_prefix='/products')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

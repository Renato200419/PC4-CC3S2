from flask import Flask
from user_management.src.controllers import user_blueprint

app = Flask(__name__)

# Registrar las rutas del controlador
app.register_blueprint(user_blueprint, url_prefix='/users')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

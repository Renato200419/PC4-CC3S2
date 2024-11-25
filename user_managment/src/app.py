from flask import Flask
from controllers import user_controller

app = Flask(__name__)

# Registrar las rutas del controlador
app.register_blueprint(user_controller)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

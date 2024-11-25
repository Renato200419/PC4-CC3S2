import requests
from repositories import ProductRepository

class ProductService:
    """Servicio para manejar la lógica de negocio de productos"""

    def __init__(self):
        self.repository = ProductRepository()

    def validate_user(self, user_id):
        """Validar la existencia de un usuario en el servicio de gestión de usuarios"""
        try:
            # Realizamos una solicitud GET al servicio de gestión de usuarios
            response = requests.get(f"http://user_management:5000/users/{user_id}")
            if response.status_code == 200:
                return True
            else:
                raise ValueError("Usuario no válido")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error al conectarse al servicio de gestión de usuarios: {e}")

    def get_all_products(self):
        """Obtener todos los productos"""
        return self.repository.get_all()

    def create_product(self, data):
        """Crear un nuevo producto, validando primero el usuario"""
        user_id = data.get('user_id')
        if not user_id:
            raise ValueError("Se requiere un 'user_id' para crear el producto.")
        if self.validate_user(user_id):
            return self.repository.create(data)

    def update_product(self, product_id, data):
        """Actualizar un producto existente"""
        return self.repository.update(product_id, data)

    def delete_product(self, product_id):
        """Eliminar un producto"""
        return self.repository.delete(product_id)

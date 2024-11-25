import requests
from product_catalog.src.repositories import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.user_service_url = 'http://user_management:5000/users'

    def create_product(self, data):
        user_id = data.get('user_id')
        # Validar existencia del usuario
        try:
            response = requests.get(f'{self.user_service_url}/{user_id}')
            if response.status_code == 200:
                return self.product_repository.create(data)
            else:
                return {'error': 'El usuario no existe'}
        except requests.exceptions.RequestException:
            return {'error': 'Servicio de usuarios no disponible'}

    def get_product(self, product_id):
        return self.product_repository.get_by_id(product_id)

    def update_product(self, product_id, data):
        return self.product_repository.update(product_id, data)

    def delete_product(self, product_id):
        return self.product_repository.delete(product_id)

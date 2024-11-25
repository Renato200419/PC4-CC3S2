from repositories import ProductRepository

class ProductService:
    """Servicio para manejar la lógica de negocio de productos"""

    def __init__(self):
        self.repository = ProductRepository()

    def get_all_products(self):
        """Obtener todos los productos"""
        return self.repository.get_all()

    def create_product(self, data):
        """Crear un nuevo producto"""
        return self.repository.create(data)

    def update_product(self, product_id, data):
        """Actualizar un producto existente"""
        return self.repository.update(product_id, data)

    def delete_product(self, product_id):
        """Eliminar un producto"""
        return self.repository.delete(product_id)

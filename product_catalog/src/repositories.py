class ProductRepository:
    """Repositorio para manejar la persistencia de productos"""

    def __init__(self):
        self.products = {}  # Diccionario simulado como base de datos
        self.counter = 1

    def get_all(self):
        """Retornar todos los productos"""
        return list(self.products.values())

    def create(self, data):
        """Crear un nuevo producto"""
        product_id = self.counter
        self.products[product_id] = {"id": product_id, **data}
        self.counter += 1
        return self.products[product_id]

    def update(self, product_id, data):
        """Actualizar un producto existente"""
        if product_id in self.products:
            self.products[product_id].update(data)
            return self.products[product_id]
        else:
            raise ValueError("Producto no encontrado")

    def delete(self, product_id):
        """Eliminar un producto"""
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Producto no encontrado")

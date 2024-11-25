from flask import Blueprint, jsonify, request
from services import ProductService

# Crear un Blueprint para el controlador
product_controller = Blueprint('product_controller', __name__)
product_service = ProductService()

@product_controller.route('/products', methods=['GET'])
def get_products():
    """Obtener todos los productos"""
    products = product_service.get_all_products()
    return jsonify(products), 200

@product_controller.route('/products', methods=['POST'])
def create_product():
    """Crear un nuevo producto"""
    data = request.get_json()
    product = product_service.create_product(data)
    return jsonify(product), 201

@product_controller.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Actualizar un producto existente"""
    data = request.get_json()
    updated_product = product_service.update_product(product_id, data)
    return jsonify(updated_product), 200

@product_controller.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Eliminar un producto por ID"""
    product_service.delete_product(product_id)
    return '', 204

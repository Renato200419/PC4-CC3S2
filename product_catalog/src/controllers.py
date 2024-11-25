from flask import Blueprint, request, jsonify
from product_catalog.src.services import ProductService

# Crear un Blueprint para el controlador
product_blueprint = Blueprint('product_controller', __name__)
product_service = ProductService()

@product_blueprint.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = product_service.create_product(data)
    if 'error' in product:
        return jsonify(product), 400
    else:
        return jsonify(product), 201

@product_blueprint.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404

@product_blueprint.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    updated_product = product_service.update_product(product_id, data)
    if updated_product:
        return jsonify(updated_product)
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404

@product_blueprint.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    result = product_service.delete_product(product_id)
    if result:
        return jsonify({'message': 'Producto eliminado'})
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404
from flask import Blueprint, jsonify, request
from services import UserService

# Crear un Blueprint para el controlador
user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['GET'])
def get_users():
    """Obtener todos los usuarios"""
    users = user_service.get_all_users()
    return jsonify(users), 200

@user_controller.route('/users', methods=['POST'])
def create_user():
    """Crear un nuevo usuario"""
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user), 201

@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Actualizar un usuario existente"""
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data)
    return jsonify(updated_user), 200

@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Eliminar un usuario por ID"""
    user_service.delete_user(user_id)
    return '', 204

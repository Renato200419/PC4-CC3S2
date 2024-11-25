from flask import Blueprint, request, jsonify
from user_management.src.services import UserService

# Crear un Blueprint para el controlador
user_blueprint = Blueprint('user_controller', __name__)
user_service = UserService()

@user_blueprint.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user), 201

@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = user_service.delete_user(user_id)
    if result:
        return jsonify({'message': 'Usuario eliminado'})
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
from repositories import UserRepository

class UserService:
    """Servicio para manejar la lógica de negocio de usuarios"""

    def __init__(self):
        self.repository = UserRepository()

    def get_all_users(self):
        """Obtener todos los usuarios"""
        return self.repository.get_all()

    def create_user(self, data):
        """Crear un nuevo usuario"""
        return self.repository.create(data)

    def update_user(self, user_id, data):
        """Actualizar un usuario existente"""
        return self.repository.update(user_id, data)

    def delete_user(self, user_id):
        """Eliminar un usuario"""
        return self.repository.delete(user_id)

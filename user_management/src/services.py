from user_management.src.repositories import UserRepository

class UserService:
    """Servicio para manejar la lógica de negocio de usuarios"""
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, data):
        return self.user_repository.create(data)

    def get_user(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def update_user(self, user_id, data):
        return self.user_repository.update(user_id, data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)
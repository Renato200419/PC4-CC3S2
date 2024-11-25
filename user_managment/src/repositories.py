class UserRepository:
    """Repositorio para manejar la persistencia de usuarios"""

    def __init__(self):
        self.users = {}  # Diccionario simulado como base de datos
        self.counter = 1

    def get_all(self):
        """Retornar todos los usuarios"""
        return list(self.users.values())

    def create(self, data):
        """Crear un nuevo usuario"""
        user_id = self.counter
        self.users[user_id] = {"id": user_id, **data}
        self.counter += 1
        return self.users[user_id]

    def update(self, user_id, data):
        """Actualizar un usuario existente"""
        if user_id in self.users:
            self.users[user_id].update(data)
            return self.users[user_id]
        else:
            raise ValueError("Usuario no encontrado")

    def delete(self, user_id):
        """Eliminar un usuario"""
        if user_id in self.users:
            del self.users[user_id]
        else:
            raise ValueError("Usuario no encontrado")

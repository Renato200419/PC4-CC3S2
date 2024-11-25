from peewee import Model, CharField, SqliteDatabase

db = SqliteDatabase('users.db')

class User(Model):
    name = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db

db.connect()
db.create_tables([User])

class UserRepository:
    def create(self, data):
        user = User.create(name=data['name'], email=data['email'])
        return {'id': user.id, 'name': user.name, 'email': user.email}

    def get_by_id(self, user_id):
        try:
            user = User.get(User.id == user_id)
            return {'id': user.id, 'name': user.name, 'email': user.email}
        except User.DoesNotExist:
            return None

    def update(self, user_id, data):
        query = User.update(**data).where(User.id == user_id)
        if query.execute():
            return self.get_by_id(user_id)
        else:
            return None

    def delete(self, user_id):
        query = User.delete().where(User.id == user_id)
        return query.execute() > 0

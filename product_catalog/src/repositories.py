from peewee import Model, CharField, IntegerField, SqliteDatabase

db = SqliteDatabase('products.db')

class Product(Model):
    name = CharField()
    description = CharField()
    user_id = IntegerField()

    class Meta:
        database = db

db.connect()
db.create_tables([Product])

class ProductRepository:
    def create(self, data):
        product = Product.create(
            name=data['name'],
            description=data['description'],
            user_id=data['user_id']
        )
        return {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'user_id': product.user_id
        }

    def get_by_id(self, product_id):
        try:
            product = Product.get(Product.id == product_id)
            return {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'user_id': product.user_id
            }
        except Product.DoesNotExist:
            return None

    def update(self, product_id, data):
        query = Product.update(**data).where(Product.id == product_id)
        if query.execute():
            return self.get_by_id(product_id)
        else:
            return None

    def delete(self, product_id):
        query = Product.delete().where(Product.id == product_id)
        return query.execute() > 0

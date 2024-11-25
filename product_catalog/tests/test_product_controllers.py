import unittest
from unittest.mock import patch
from product_catalog.src.app import app

class TestProductControllers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('src.services.ProductService.create_product')
    def test_create_product(self, mock_create_product):
        mock_create_product.return_value = {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        }
        response = self.app.post('/products/', json={
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        })

    @patch('src.services.ProductService.get_product')
    def test_get_product(self, mock_get_product):
        mock_get_product.return_value = {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        }
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        })

    @patch('src.services.ProductService.update_product')
    def test_update_product(self, mock_update_product):
        mock_update_product.return_value = {
            'id': 1,
            'name': 'Producto A Actualizado',
            'description': 'Descripción Actualizada',
            'user_id': 1
        }
        response = self.app.put('/products/1', json={
            'name': 'Producto A Actualizado',
            'description': 'Descripción Actualizada'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            'id': 1,
            'name': 'Producto A Actualizado',
            'description': 'Descripción Actualizada',
            'user_id': 1
        })

    @patch('src.services.ProductService.delete_product')
    def test_delete_product(self, mock_delete_product):
        mock_delete_product.return_value = True
        response = self.app.delete('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Producto eliminado'})

if __name__ == '__main__':
    unittest.main()

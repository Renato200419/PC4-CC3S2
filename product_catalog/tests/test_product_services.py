import unittest
from unittest.mock import patch
from product_catalog.src.services import ProductService

class TestProductServices(unittest.TestCase):
    def setUp(self):
        self.product_service = ProductService()

    @patch('requests.get')
    @patch('src.repositories.ProductRepository.create')
    def test_create_product(self, mock_create, mock_requests_get):
        mock_requests_get.return_value.status_code = 200
        mock_create.return_value = {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        }
        product = self.product_service.create_product({
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        })
        self.assertEqual(product, {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        })

    @patch('src.repositories.ProductRepository.get_by_id')
    def test_get_product(self, mock_get_by_id):
        mock_get_by_id.return_value = {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        }
        product = self.product_service.get_product(1)
        self.assertEqual(product, {
            'id': 1,
            'name': 'Producto A',
            'description': 'Descripción',
            'user_id': 1
        })

    @patch('src.repositories.ProductRepository.update')
    def test_update_product(self, mock_update):
        mock_update.return_value = {
            'id': 1,
            'name': 'Producto A Actualizado',
            'description': 'Descripción Actualizada',
            'user_id': 1
        }
        updated_product = self.product_service.update_product(1, {
            'name': 'Producto A Actualizado',
            'description': 'Descripción Actualizada'
        })
        self.assertEqual(updated_product, {
            'id': 1,
            'name': 'Producto A Actualizado',
            'description': 'Descripción Actualizada',
            'user_id': 1
        })

    @patch('src.repositories.ProductRepository.delete')
    def test_delete_product(self, mock_delete):
        mock_delete.return_value = True
        result = self.product_service.delete_product(1)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

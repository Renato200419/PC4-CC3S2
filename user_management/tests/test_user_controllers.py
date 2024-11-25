import unittest
from unittest.mock import patch
from user_management.src.app import app

class TestUserControllers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('src.services.UserService.create_user')
    def test_create_user(self, mock_create_user):
        mock_create_user.return_value = {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        }
        response = self.app.post('/users/', json={
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        })

    @patch('src.services.UserService.get_user')
    def test_get_user(self, mock_get_user):
        mock_get_user.return_value = {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        }
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        })

    @patch('src.services.UserService.update_user')
    def test_update_user(self, mock_update_user):
        mock_update_user.return_value = {
            'id': 1,
            'name': 'Sebastián Pérez Actualizado',
            'email': 'se12pe@gmail.com'
        }
        response = self.app.put('/users/1', json={
            'name': 'Sebastián Pérez Actualizado'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            'id': 1,
            'name': 'Sebastián Pérez Actualizado',
            'email': 'se12pe@gmail.com'
        })

    @patch('src.services.UserService.delete_user')
    def test_delete_user(self, mock_delete_user):
        mock_delete_user.return_value = True
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Usuario eliminado'})

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from user_management.src.services import UserService

class TestUserServices(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()

    @patch('src.repositories.UserRepository.create')
    def test_create_user(self, mock_create):
        mock_create.return_value = {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        }
        user = self.user_service.create_user({
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        })
        self.assertEqual(user, {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        })

    @patch('src.repositories.UserRepository.get_by_id')
    def test_get_user(self, mock_get_by_id):
        mock_get_by_id.return_value = {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        }
        user = self.user_service.get_user(1)
        self.assertEqual(user, {
            'id': 1,
            'name': 'Sebastián Pérez',
            'email': 'se12pe@gmail.com'
        })

    @patch('src.repositories.UserRepository.update')
    def test_update_user(self, mock_update):
        mock_update.return_value = {
            'id': 1,
            'name': 'Sebastián Pérez Actualizado',
            'email': 'se12pe@gmail.com'
        }
        updated_user = self.user_service.update_user(1, {
            'name': 'Sebastián Pérez Actualizado'
        })
        self.assertEqual(updated_user, {
            'id': 1,
            'name': 'Sebastián Pérez Actualizado',
            'email': 'se12pe@gmail.com'
        })

    @patch('src.repositories.UserRepository.delete')
    def test_delete_user(self, mock_delete):
        mock_delete.return_value = True
        result = self.user_service.delete_user(1)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

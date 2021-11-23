import json
import unittest

from werkzeug.datastructures import Headers
from Hotel import create_app, db



class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name = 'testing')
        self.client = self.app.test_client
        self.user_data = {
            "username": "test",
            "password": "test123",
            "email": "test@test.com"
        }

        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login(self):
        url = "/users"
        res = self.client().post(
            url,
            data = self.user_data
        )
        url = "/auth/login"
        res = self.client().post(
            url,
            data = json.dumps({"username": "test", "password": "test123"}),
            headers = {"Content-Type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text = True))
        self.assertIn('access_token', res_data)

    def test_login_failed(self):
        url = "/users"
        res = self.client().post(
            url,
            data = self.user_data
        )
        url = "/auth/login"
        res = self.client().post(
            url,
            data = json.dumps({"username": "test", "password": "wrongpass"}),
            headers = {"Content-Type": "application/json"}
        )
        self.assertEqual(res.status_code, 401)
        res_data = json.loads(res.get_data(as_text = True))
        data = {
            
            "description": "Invalid credentials",
            "error": "Bad Request",
            "status_code": 401
        }
        self.assertEqual(res_data, data)
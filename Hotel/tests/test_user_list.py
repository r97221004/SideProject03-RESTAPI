import json
import unittest
from Hotel import create_app, db


class TestUserList(unittest.TestCase):
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

    
    def test_user_create(self):
        url = "/users"
        res = self.client().post(
            url,
            data = self.user_data
        )

        self.assertEqual(res.status_code, 201)
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res_data.get('username'), self.user_data['username'])
        self.assertEqual(res_data.get('email'), self.user_data['email'])

        res = self.client().post(
            url,
            data = self.user_data
        )

        self.assertEqual(res.status_code, 409)
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res_data.get('message'), "username exists.")


    def test_user_get(self):
        # create user
        url = "/users"
        res = self.client().post(
            url,
            data = self.user_data
        )
        # user login
        url = "/auth/login"
        res = self.client().post(
            url,
            data = json.dumps({"username": "test", "password": "test123"}),
            headers = {"Content-Type": "application/json"}
        )
        res_data = json.loads(res.get_data(as_text = True))
        access_token = f"{self.app.config['JWT_AUTH_HEADER_PREFIX']} {res_data['access_token']}"
        # get user list
        url = "/users"
        res = self.client().get(
            url,
            headers = {'Authorization': access_token}
        )
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res_data), 1)



    





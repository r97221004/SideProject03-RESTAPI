import json
from Hotel.tests.base import TestBase 

class TestUser(TestBase):

    def test_user_put(self):
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
        # modify user list
        url = f"/user/{self.user_data['username']}"
        res = self.client().put(
            url,
            headers = {'Authorization': access_token},
            data = {
                "password":"test456",
                "email":"test456@test.com"
            }
        )
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['email'], "test456@test.com")
        self.assertEqual(res_data['from_admin'], False)

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
        # get user
        url = f"/user/{self.user_data['username']}"
        res = self.client().get(
            url,
            headers = {'Authorization': access_token},

        )
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['username'], "test")
        self.assertEqual(res_data['email'], "test@test.com")
    
    def test_user_get_not_exist(self):
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
        # get user
        url = f"/user/wrongusername"
        res = self.client().get(
            url,
            headers = {'Authorization': access_token},

        )
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data['message'], "user not found")

    def test_user_delete(self):
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
        # delete user
        url = f"/user/{self.user_data['username']}"
        res = self.client().delete(
            url,
            headers = {'Authorization': access_token},

        )
        res_data = res.get_data(as_text = True)
        self.assertEqual(res.status_code, 204)
        self.assertEqual(res_data, '')

    def test_user_delete_with_wrong_token(self):
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
        # delete user with wrong token
        url = f"/user/wrongusername"
        res = self.client().delete(
            url,
            headers = {'Authorization': access_token},

        )
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['message'], 'Please use the right token.')

    def test_user_update(self):
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
        # update user
        url = f"/user/{self.user_data['username']}"
        res = self.client().patch(
            url,
            headers = {'Authorization': access_token},
            data = {'email':'test123@test.com'}

        )
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['email'], 'test123@test.com')
    
    def test_user_update_with_wrong_token(self):
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
        # update user with wrong token
        url = f"/user/wrongusername"
        res = self.client().patch(
            url,
            headers = {'Authorization': access_token},
            data = {'email':'test123@test.com'}

        )
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['message'], 'Please use the right token.')


from fastapi import status

from settings import HOST_URL
from tests.tests_routes.common_functionaly import Requester


class TestUsersRoutes(Requester):
    user_url = f"{HOST_URL}/user"

    sign_user_up_url = f"{user_url}/signup"
    sign_use_in_url = f"{user_url}/signin"

    def test_sign_user_up__1(self):
        data = {
            "email":    "fastapi@packt.com",
            "password": "Stro0ng!",
            "username": "FastPackt"
        }
        response = self.send_request(url=self.sign_user_up_url, method="POST", json_data=data)
        assert response["message"] == "User successfully registered!"

    def test_sign_user_up__2(self):
        data = {
            "email":    "fastapi@packt.com",
            "password": "Stro0ng!",
            "username": "FastPackt"
        }
        response = self.send_request(url=self.sign_user_up_url, method="POST", json_data=data)
        assert response["status_code"] == status.HTTP_409_CONFLICT

    def test_sign_use_in__1(self):
        data = {
            "email":    "fastapi@packt.com",
            "password": "Stro0ng!"
        }
        response = self.send_request(url=self.sign_use_in_url, method="POST", json_data=data)
        assert response["message"] == "User signed in successfully"

    def test_sign_use_in__2(self):
        data = {
            "email":    "fastapi@packt.com",
            "password": "password"
        }
        response = self.send_request(url=self.sign_use_in_url, method="POST", json_data=data)
        assert response["status_code"] == status.HTTP_403_FORBIDDEN

    def test_sign_use_in__3(self):
        data = {
            "email":    "f@packt.com",
            "password": "password"
        }
        response = self.send_request(url=self.sign_use_in_url, method="POST", json_data=data)
        assert response["status_code"] == status.HTTP_404_NOT_FOUND

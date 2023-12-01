from fastapi import HTTPException, status

from settings import HOST_URL
from tests.tests_routes.common_functionaly import Requester


class TestUsersRoutes(Requester):
    user_url = f"{HOST_URL}/user"
    sign_new_user_url = f"{user_url}/signup"

    def test_sign_user_up(self):
        # try:
        data = {
            "email":    "fastapi@packt.com",
            "password": "Stro0ng!",
            "username": "FastPackt"
        }
        response = self.send_request(url=self.sign_new_user_url, method="POST", json_data=data)
        assert response["message"] == "User successfully registered!"
        # except HTTPException as exception:
        #     print(f'{exception = }')
        #     # assert exception["status_code"] == status.HTTP_409_CONFLIC
        #     # assert exception["detail"] == "User with supplied username exists"
        #
        # except Exception as exception:
        #     print(f'{exception = }')
        #     raise exception
        #     # assert exception["status_code"] == status.HTTP_409_CONFLIC
        #     # assert exception["detail"] == "User with supplied username exists"

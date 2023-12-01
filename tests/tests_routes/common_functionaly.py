import requests


class Requester:
    RESPONSE_TIMEOUT = 5

    @classmethod
    def send_request(cls, url, method="GET", json_data=None):
        response = None

        try:
            response = requests.request(method,
                                        url,
                                        headers={
                                            "Content-Type": "application/json",
                                            "Accept": "application/json",
                                        },
                                        timeout=cls.RESPONSE_TIMEOUT,
                                        json=json_data)

            assert response.status_code == 200

            return response.json()

        except AssertionError:
            return {"status_code": response.status_code}
        except Exception as exception:
            raise exception

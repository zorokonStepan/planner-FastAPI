from fastapi import status

from settings import HOST_URL
from tests.tests_routes.common_functionaly import Requester


class TestEventsRoutes(Requester):
    event_url = f"{HOST_URL}/event"

    create_event_url = f"{event_url}/new"
    single_event_url = lambda self, id_event: f"{self.event_url}/{id_event}"

    data_1 = {
        "id":          1,
        "title":       "FastAPI Book Launch",
        "image":       "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of the FastAPI book in this event."
                       "Ensure to comewith your own copy to win gifts!",
        "tags":        ["python", "fastapi", "book", "launch"],
        "location":    "Google Meet"
    }

    def test_retrieve_all_events(self):
        response = self.send_request(url=self.event_url)
        assert type(response) == list

    def test_create_event(self):
        response = self.send_request(url=self.create_event_url, method="POST", json_data=self.data_1)
        assert response["message"] == "Event created successfully"

    def test_retrieve_event__1(self):
        response = self.send_request(url=self.single_event_url(1))
        assert response == self.data_1

    def test_retrieve_event__2(self):
        response = self.send_request(url=self.single_event_url(2))
        assert response["status_code"] == status.HTTP_404_NOT_FOUND

    def test_delete_event__1(self):
        response = self.send_request(url=self.single_event_url(1), method="DELETE")
        assert response["message"] == "Event deleted successfully"

    def test_delete_event__2(self):
        response = self.send_request(url=self.single_event_url(2), method="DELETE")
        assert response["status_code"] == status.HTTP_404_NOT_FOUND

    def test_delete_all_events(self):
        response = self.send_request(url=self.event_url, method="DELETE")
        assert response["message"] == "Events deleted successfully"

from django.test import TestCase, Client

class TestEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = Client()


    def test_endpoint_is_working(self):
        response = self.client.get("/api/company")
        assert response.status_code == 200
    

    def test_url_not_found(self):
        response = self.client.get("/api/companyy")
        assert response.status_code == 404

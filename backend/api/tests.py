from django.test import TestCase
from ninja.testing import TestClient
# import requests

from .endpoints import router


class TestEndpoint(TestCase):
    def test_all_companies(self):
        client = TestClient(router)
        response = client.get("http://localhost:8000/api/company")
        # assert response.status_code == 200

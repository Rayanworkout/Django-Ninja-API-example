from django.test import TestCase, Client
from api.models import Company


class TestEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        # Create a company
        Company.objects.create(
            rank=1,
            organizationName="Apple",
            country="USA",
            revenue=274515,
            profits=57410,
            assets=338516,
            marketValue=905600,
        )

        Company.objects.create(
            rank=2,
            organizationName="Sinopec",
            country="china",
            revenue=143015,
            profits=39240,
            assets=286556,
            marketValue=1024800,
        )


        Company.objects.create(
            rank=2,
            organizationName="Siemens",
            country="germany",
            revenue=147015,
            profits=39240,
            assets=356556,
            marketValue=1014800,
        )

    def test_endpoint_is_working(self):
        response = self.client.get("/api/company")
        assert response.status_code == 200

    def test_url_not_found(self):
        response = self.client.get("/api/companyy")
        assert response.status_code == 404

    def test_company_created(self):
        company = Company.objects.get(organizationName="Apple")
        assert company is not None

    def test_filter_by_country(self):

        response = self.client.get("/api/company?country=usa")

        assert response.status_code == 200

        assert len(response.json()) == 1

        assert response.json()[0]["organizationName"] == "Apple"
    

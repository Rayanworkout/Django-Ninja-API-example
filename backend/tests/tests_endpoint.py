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

        Company.objects.create(
            rank=2,
            organizationName="Hyundai",
            country="South Korea",
            revenue=247015,
            profits=49240,
            assets=356556,
            marketValue=1074800,
        )

        Company.objects.create(
            rank=2,
            organizationName="HSBC Holdings",
            country="United Kingdom",
            revenue=97015,
            profits=39240,
            assets=356556,
            marketValue=1014800,
        )

    def test_endpoint_is_working(self):
        response = self.client.get("/api/company")
        assert response.status_code == 200

    def test_url_not_found(self):
        response = self.client.get("/api/companyy")
        self.assertEqual(response.status_code, 404)

    def test_company_created(self):
        company = Company.objects.get(organizationName="Apple")
        self.assertIsNotNone(company)
        self.assertEqual(company.country, "USA")

    def test_filter_by_country(self):

        response = self.client.get("/api/company?country=usa")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.json()), 1)

        self.assertEqual(response.json()[0]["organizationName"], "Apple")

    def test_filter_by_revenue(self):

        response = self.client.get("/api/company?revenue=100000")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.json()), 4)

    def test_filter_by_country_and_revenue(self):
        response = self.client.get("/api/company?country=usa&revenue=100000")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.json()), 1)

        self.assertEqual(response.json()[0]["organizationName"], "Apple")
    
    def test_order_by_revenue(self):
        response = self.client.get("/api/company?order_by=revenue")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.json()), 5)

        self.assertEqual(response.json()[0]["organizationName"], "HSBC Holdings")

from django.test import TestCase

from api.models import Company
from api.companies_statistics import CompaniesStatistics


class TestStatistics(TestCase):

    def setUp(self) -> None:
        self.statistics = CompaniesStatistics()

        Company.objects.create(
            rank=1,
            organizationName="Apple",
            country="USA",
            revenue=274515000000,  # $274.515 billion
            profits=157410000000,  # $157.41 billion
            assets=338516000000,  # $338.516 billion
            marketValue=905600000000,  # $905.6 billion
        )

        Company.objects.create(
            rank=2,
            organizationName="Hyundai",
            country="South Korea",
            revenue=247015000000,  # $247.015 billion
            profits=49240000000,  # $49.24 billion
            assets=356556000000,  # $356.556 billion
            marketValue=1074800000000,  # $1.0748 trillion
        )

        Company.objects.create(
            rank=3,
            organizationName="Siemens",
            country="Germany",
            revenue=147015000000,  # $147.015 billion
            profits=39240000000,  # $39.24 billion
            assets=356556000000,  # $356.556 billion
            marketValue=1014800000000,  # $1.0148 trillion
        )

        Company.objects.create(
            rank=4,
            organizationName="Sinopec",
            country="China",
            revenue=143010000000,  # $143.01 billion
            profits=39240000000,  # $39.24 billion
            assets=286556000000,  # $286.556 billion
            marketValue=1024800000000,  # $1.0248 trillion
        )

        Company.objects.create(
            rank=5,
            organizationName="HSBC Holdings",
            country="United Kingdom",
            revenue=97015000000,  # $97.015 billion
            profits=49240000000,  # $49.24 billion
            assets=356556000000,  # $356.556 billion
            marketValue=1014800000000,  # $1.0148 trillion
        )

        Company.objects.create(
            rank=6,
            organizationName="JPMorgan Chase",
            country="USA",
            revenue=274515000000,  # $274.515 billion
            profits=157410000000,  # $157.41 billion
            assets=338516000000,  # $338.516 billion
            marketValue=905600000000,  # $905.6 billion
        )

    def test_country_mean_revenue(self):
        country = "USA"
        field = "revenue"
        mean = self.statistics.get_country_mean(country, field)
        expected_result = {"mean": 274515000000.0, "country": "USA", "field": "revenue"}
        self.assertEqual(mean, expected_result)

    def test_country_mean_profits(self):
        country = "USA"
        field = "profits"
        mean = self.statistics.get_country_mean(country, field)
        expected_result = {"mean": 157410000000.0, "country": "USA", "field": "profits"}
        self.assertEqual(mean, expected_result)

    def test_country_mean_bad_field(self):
        country = "USA"
        field = "bad_field"
        mean = self.statistics.get_country_mean(country, field)
        self.assertIsNone(mean)

    def test_country_mean_bad_country(self):
        country = "bad_country"
        field = "revenue"
        mean = self.statistics.get_country_mean(country, field)
        self.assertIsNone(mean)

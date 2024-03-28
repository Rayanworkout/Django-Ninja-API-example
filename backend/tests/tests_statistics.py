from django.test import TestCase

from api.statistics import Statistics


class TestStatistics(TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_standard_deviation(self):
        values = [2, 4, 6, 8, 10]
        standard_deviation = self.statistics.standard_deviation(values)
        assert round(standard_deviation, 2) == 2.83
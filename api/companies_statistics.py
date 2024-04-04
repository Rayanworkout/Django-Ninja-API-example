import statistics


from functools import lru_cache
from math import sqrt

from .models import Company

class CompaniesStatistics:
    """
    Various statistical functions used to compute the mean, median, standard deviation, etc. of the data.

    The results are cached using the LRU cache mechanism to improve performance.

    """

    def __standard_deviation(self, values: list[float]) -> float:
        """

        # THIS METHOD WON'T BE USED IN THE FINAL IMPLEMENTATION, BECAUSE IT ALREADY EXISTS IN THE STATISTICS MODULE


        Function used to compute the standard deviation of a list of values. In our case,
        standard deviation can be applied on the following fields: revenue, profits, assets, marketValue.

        The standard deviation is a measure of the amount of variation or dispersion of a set of values.
        A low standard deviation means that most of the numbers are close to the average.
        A high standard deviation means that the numbers are spread out.

        Example:

        Let's say we have the following set of revenues (in billions) for 5 companies:

        revenues = [2, 4, 6, 8, 10]

        The standard deviation of the revenues can be computed as follows:

        - We first compute the mean of the revenues:

        mean = (2 + 4 + 6 + 8 + 10) / 5 = 6

        - Then, we compute the variance of the revenues (average of the squared difference from the mean)

        variance = [(2 - 6) ** 2 + (4 - 6) ** 2 + (6 - 6) ** 2 + (8 - 6) ** 2 + (10 - 6) ** 2] / 5 = 8

        - Finally, we compute the standard deviation as the square root of the variance:

        standard_deviation = sqrt(8) = 2.83

        """

        # compute the mean of the values
        mean = statistics.mean(values)

        # compute the variance of the values
        variance = sum((x - mean) ** 2 for x in values) / len(values)

        # return the square root of the variance
        return sqrt(variance)

    @lru_cache(maxsize=1024)
    def get_country_standard_deviation(self, country: str, field: str):
        """
        Function used to compute the standard deviation of a specific field for a specific country.

        """

        # filter the companies in the given country
        companies = Company.objects.filter(country=country)

        if (
            field in ["revenue", "profits", "assets", "marketValue"]
            and companies.exists()
        ):
            # extract the values of the given field
            values = [float(getattr(company, field)) for company in companies]

            # compute the standard deviation of the values
            standard_deviation = statistics.stdev(values)

            return {
                "standard_deviation": standard_deviation,
                "country": country,
                "field": field,
            }

    @lru_cache(maxsize=1024)
    def get_country_mean(self, country: str, field: str):
        """
        Function used to compute the mean of a specific field for a specific country.

        """

        # filter the companies in the given country
        companies = Company.objects.filter(country=country)

        if (
            field in ["revenue", "profits", "assets", "marketValue"]
            and companies.exists()
        ):
            # extract the values of the given field
            values = [float(getattr(company, field)) for company in companies]

            # compute the mean of the values
            mean = statistics.mean(values)

            return {
                "mean": mean,
                "country": country,
                "field": field,
            }

from .models import Company
from math import sqrt


# statistics about a country (mean and median)


class Statistics:

    def standard_deviation(self, values: list[float]) -> float:
        """
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
        mean = sum(values) / len(values)

        # compute the variance of the values
        variance = sum((x - mean) ** 2 for x in values) / len(values)

        # return the square root of the variance
        return sqrt(variance)

    def get_country_mean(self, country, field):
        """
        Function used to compute the mean of a specific field for a specific country.

        """

        # filter the companies in the given country
        companies = Company.objects.filter(country=country)

        # extract the values of the given field
        values = [getattr(company, field) for company in companies]

        # compute the mean of the values
        mean = sum(values) / len(values)

        return mean
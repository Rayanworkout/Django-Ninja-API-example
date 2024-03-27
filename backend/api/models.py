from django.db import models


class CompanyRecord(models.Model):
    rank = models.IntegerField()
    organizationName = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    revenue = models.DecimalField(max_digits=20, decimal_places=2)
    profits = models.DecimalField(max_digits=20, decimal_places=2)
    assets = models.DecimalField(max_digits=20, decimal_places=2)
    marketValue = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.organizationName

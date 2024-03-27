from ninja import ModelSchema, FilterSchema
from typing import Optional

from .models import CompanyRecord


class CompanySchema(ModelSchema):
    """
    Response schema for CompanyRecord, I automatically generate the schema from the model.

    https://django-ninja.dev/guides/response/
    """

    class Meta:
        model = CompanyRecord
        fields = "__all__"


class CompanyFilterSchema(FilterSchema):
    """
    Filter schema for CompanyRecord

    https://django-ninja.dev/guides/input/filtering/
    """

    rank: Optional[int] = None
    organizationName: Optional[str] = None
    country: Optional[str] = None
    revenue: Optional[str] = None
    profits: Optional[str] = None
    assets: Optional[str] = None
    marketValue: Optional[str] = None

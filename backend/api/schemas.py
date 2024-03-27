from ninja import ModelSchema, FilterSchema
from pydantic import Field
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

    min_rank: Optional[int] = Field(None, q="rank__gte")
    max_rank: Optional[int] = Field(None, q="rank__lte")

    name: Optional[str] = Field(None, q="organizationName__icontains")

    country: Optional[str] = Field(None, q="country__icontains")

    revenue: Optional[str] = Field(None, q="revenue__gte")

    profits: Optional[str] = None

    assets: Optional[str] = None

    marketValue: Optional[str] = None

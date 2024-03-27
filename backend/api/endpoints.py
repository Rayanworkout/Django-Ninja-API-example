# from functools import lru_cache
from ninja import NinjaAPI, Query
from .models import CompanyRecord
from .schemas import CompanySchema, CompanyFilterSchema

from typing import List

# Creating an instance of NinjaAPI
api = NinjaAPI()


@api.get("/company", response=List[CompanySchema], tags=["Company"])
def company(
    request,
    filters: CompanyFilterSchema = Query(...),
    order_by: str = "asc",
    limit: int = None,
):
    """
    Return a list of companies according to the filters provided.

    If no filters are provided, return all companies.
    """

    companies = CompanyRecord.objects.all()
    companies = filters.filter(companies)

    if order_by == "asc":
        companies = companies.order_by("rank")
    elif order_by == "desc":
        companies = companies.order_by("-rank")

    if limit:
        companies = companies[:limit]

    return companies

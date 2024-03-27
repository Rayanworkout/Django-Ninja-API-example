# from functools import lru_cache
from ninja import NinjaAPI, Query
from .models import CompanyRecord
from .schemas import CompanySchema, CompanyFilterSchema

from typing import List

# Creating an instance of NinjaAPI
api = NinjaAPI()


@api.get("/company", response=List[CompanySchema], tags=["Company"])
def company(request, filters: CompanyFilterSchema = Query(...)):
    """
    Return a list of companies according to the filters provided.

    If no filters are provided, return all companies.
    """

    companies = CompanyRecord.objects.all()
    companies = filters.filter(companies)

    return companies

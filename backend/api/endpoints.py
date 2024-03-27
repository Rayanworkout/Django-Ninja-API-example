# from functools import lru_cache

from ninja import NinjaAPI
from .models import CompanyRecord
from .schemas import CompanySchema

from typing import List

# Creating an instance of NinjaAPI
api = NinjaAPI()


@api.get("/company", response=List[CompanySchema], tags=["Company"])
def company(request):
    """Return all companies in the database."""

    companies = CompanyRecord.objects.all()

    return companies

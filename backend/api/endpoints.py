# from functools import lru_cache
from ninja import NinjaAPI, Query, Router
from .models import Company
from .schemas import CompanySchema, CompanyFilterSchema

from typing import List

# Creating an instance of NinjaAPI
api = NinjaAPI()
router = Router()


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

    Allowed Filters:

    > rank: the rank of the company in the list

    > min_rank: the minimum rank of the company, for instance min_rank=10 will return companies with rank >= 10

    > max_rank: the maximum rank of the company, for instance max_rank=10 will return companies with rank <= 10

    > name: the name of the company, it will match partially. Example: name=hsbc will return HSBC Holdings.

    > country: the country of the company, it will match partially. Example: country=united will return companies from United States, United Kingdom, etc.

    > revenue: the revenue of the company, it will match greater than or equal to. Example: revenue=100 will return companies with revenue >= 100

    > order_by: the field to order the companies by. Allowed values: asc, desc, organizationName, revenue, profits, assets, marketValue

    > limit: the maximum number of companies to return

    All filters can be combined, for instance, to get the top 10 companies from the United States with revenue >= 100, you can use:
    > /company?country=united&revenue=100&limit=10

    If you want to order the companies by revenue in ascending order, you can use:
    > /company?order_by=revenue

    If you want to get the top 10 companies with the highest revenue, you can use:
    > /company?order_by=revenue&limit=10

    """

    companies = Company.objects.all()
    companies = filters.filter(companies)

    match order_by:
        case "asc":
            companies = companies.order_by("rank")
        case "desc":
            companies = companies.order_by("-rank")

        case "organizationName" | "revenue" | "profits" | "assets" | "marketValue":
            companies = sorted(companies, key=lambda x: getattr(x, order_by))

        case _:
            companies = companies.order_by("rank")

    if limit:
        companies = companies[:limit]

    return companies


api.add_router("", router)

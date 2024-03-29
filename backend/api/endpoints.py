# from functools import lru_cache
from ninja import NinjaAPI, Query
from .models import Company
from .schemas import CompanySchema, CompanyFilterSchema

from typing import List

# Creating an instance of NinjaAPI
api = NinjaAPI()


@api.get("/companies", response=List[CompanySchema], tags=["Company"])
def company(
    request,
    filters: CompanyFilterSchema = Query(...),
    order: str = "asc",
    order_by: str = None,
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

    > order: Ascending or Descending order. Allowed values: asc, desc

    > order_by: the field to order the companies by. Allowed values: organizationName, revenue, profits, assets, marketValue

    > limit: the maximum number of companies to return

    All filters can be combined, for instance, to get the top 10 companies from the United States with revenue >= 100, you can use:
    > /companies?country=united%20states&revenue=100&limit=10

    If you want to order the companies by revenue in ascending order, you can use:
    > /companies?order_by=revenue

    If you want to get the top 10 companies with the highest revenue, you can use:
    > /companies?order_by=revenue&limit=10

    """

    companies = Company.objects.all()
    companies = filters.filter(companies)

    if order == "desc":
        companies = companies.order_by("-rank")
    else:
        companies = companies.order_by("rank")

    if order_by in ["organizationName", "revenue", "profits", "assets", "marketValue"]:
        companies = sorted(companies, key=lambda x: getattr(x, order_by))

    if limit:
        companies = companies[:limit]

    return companies

# from functools import lru_cache

from django.http import JsonResponse

from ninja import NinjaAPI
from .models import CompanyRecord

# Creating an instance of NinjaAPI
api = NinjaAPI()


@api.get("/company")
def company(request, rank: int = 0):
    """Return all companies in the database."""
    if rank > 0:
        data = CompanyRecord.objects.filter(rank=rank).values()
        
        return JsonResponse(list(data), safe=False)

    data = CompanyRecord.objects.all().values()

    return JsonResponse(list(data), safe=False)

from functools import lru_cache

from ninja import NinjaAPI
from .csv_parser import parser

# Creating an instance of NinjaAPI
api = NinjaAPI()

# Parsing the CSV file
df = parser()

@api.get("/hello")
def hello(request):
    return df

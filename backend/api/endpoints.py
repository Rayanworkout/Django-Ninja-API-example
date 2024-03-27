from functools import lru_cache

from ninja import NinjaAPI
from csv_parser.csv_parser import Parser

# Creating an instance of NinjaAPI
api = NinjaAPI()

# Parsing the CSV file
parser = Parser()
# df = parser.csv_to_database()


# @api.get("/all_companies")
# def all(request, rank: int = 0):
#     return df.to_dict(orient="records")[rank - 1]

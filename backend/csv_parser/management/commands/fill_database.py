from django.core.management.base import BaseCommand
from ... import csv_parser


class Command(BaseCommand):
    help = "Parse the CSV file and insert its content into the database."

    def handle(self, *args, **options):
        print("Filling the database with the CSV file...")
        parser = csv_parser.Parser()
        parser.csv_to_database()

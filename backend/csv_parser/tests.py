import os
import pandas as pd

from django.test import TestCase
from .csv_parser import Parser

from api.models import Company


class TestParser(TestCase):

    def setUp(self) -> None:
        self.parser = Parser()

    ############ INIT ############
    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            _ = Parser(file_path="not_existing.csv")

    def test_default_file_path(self):
        current_directory = os.path.dirname(__file__)
        self.assertEqual(
            self.parser.file_path, os.path.join(current_directory, "data.csv")
        )

    ############ PARSE_CSV ############
    def test_parse_csv(self):
        df = self.parser._Parser__parse_csv()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2051, 7))

    def test_clean_dataframe(self):
        df = self.parser._Parser__parse_csv()
        df = self.parser._Parser__clean_dataframe(df)
        self.assertEqual(df.shape, (1999, 7))
        self.assertFalse(df.isnull().values.any())
        self.assertFalse(df.duplicated().any())
    

    ############ CSV_TO_DATABASE ############
    def test_csv_to_database(self):
        self.parser.csv_to_database()
        self.assertEqual(Company.objects.count(), 1999)

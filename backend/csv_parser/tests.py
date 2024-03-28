import os
import pandas as pd

from django.test import TestCase
from .csv_parser import Parser


class TestParser(TestCase):

    ############ INIT ############
    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            _ = Parser(file_path="not_existing.csv")

    def test_default_file_path(self):
        parser = Parser()
        current_directory = os.path.dirname(__file__)
        self.assertEqual(parser.file_path, os.path.join(current_directory, "data.csv"))


    ############ PARSE_CSV ############
    def test_parse_csv(self):
        parser = Parser()
        df = parser._Parser__parse_csv()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2051, 7))
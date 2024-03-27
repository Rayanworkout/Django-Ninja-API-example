import os
import pandas as pd


class Parser:
    def __init__(self, file_path: str = "data.csv") -> None:

        file_path = os.path.join(os.path.dirname(__file__), file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File {file_path} not found, please place your csv file in the same directory as the script."
            )
        
        self.file_path = file_path

    def parse_csv(self) -> pd.DataFrame:
        """Parse the csv file and return a pandas DataFrame.

        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        """

        return pd.read_csv(self.file_path)

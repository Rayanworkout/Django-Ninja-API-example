import os
import pandas as pd


def parser(file_path: str = "data_companies.csv") -> pd.DataFrame:
    """Parse the csv file and return a pandas DataFrame.

    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    """

    file_path = os.path.join(os.path.dirname(__file__), file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File {file_path} not found, please place your csv file in the same directory as the script."
        )

    return pd.read_csv(file_path)

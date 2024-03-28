import os
import pandas as pd

from api.models import Company


class Parser:
    def __init__(self, file_path: str = "data.csv") -> None:

        file_path = os.path.join(os.path.dirname(__file__), file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File {file_path} not found, please place your csv file in the same directory as the script."
            )

        self.file_path = file_path

    def __parse_csv(self) -> pd.DataFrame:
        """Parse the csv file and return a pandas DataFrame.

        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        """

        return pd.read_csv(self.file_path)

    def __clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Cleans the dataframe by removing missing values, duplicates, and converting the 'B' and 'M' values to numbers."""

        # Drop rows with missing values
        df = df.dropna()

        # Drop duplicate rows
        df = df.drop_duplicates()

        # Clean the 'B' values in the specified columns
        def clean_and_convert(value):
            if "B" in value:
                return (
                    float(value.replace(" B", "").replace(",", "")) * 1e9
                )  # Convert to billions
            elif "M" in value:
                return (
                    float(value.replace(" M", "").replace(",", "")) * 1e6
                )  # Convert to millions
            else:
                return float(value.replace(",", ""))

        # Apply the function to clean and convert the 'B' and 'M' values in the specified columns
        columns_to_clean = ["rank", "revenue", "profits", "assets", "marketValue"]

        for column in columns_to_clean:
            df[column] = df[column].apply(clean_and_convert)

        return df

    def csv_to_database(self) -> None:
        """Saves the data to the database."""

        data = self.__parse_csv()
        data = self.__clean_dataframe(data)

        for _, row in data.iterrows():
            Company.objects.create(
                rank=row["rank"],
                organizationName=row["organizationName"],
                country=row["country"],
                revenue=row["revenue"],
                profits=row["profits"],
                assets=row["assets"],
                marketValue=row["marketValue"],
            )

        print("Data successfully saved to the database.")

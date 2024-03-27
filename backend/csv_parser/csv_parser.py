import os
import pandas as pd

from .models import CompanyRecord

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


    def clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the data before saving it to the database."""

        # Drop rows with missing values
        df = df.dropna()

        # Drop duplicate rows
        df = df.drop_duplicates()

        # Clean the 'B' values in the specified columns
        columns_to_clean = ['revenue', 'profits', 'assets', 'marketValue']

        for column in columns_to_clean:
            # I replace ' B' with an empty string and remove commas
            df[column] = df[column].str.replace(' B', '').str.replace(',', '')


        return df
    

    def csv_to_database(self) -> None:
        """Parse the csv file and save the data to the database."""

        data = self.__parse_csv()

        for index, row in data.iterrows():
            CompanyRecord.objects.create(
                rank=row["rank"],
                organizationName=row["organizationName"],
                country=row["country"],
                revenue=row["revenue"],
                profits=row["profits"],
                assets=row["assets"],
                marketValue=row["marketValue"]
            )

        print("Data successfully saved to the database.")



d = Parser()
df = d.parse_csv()
print(d.clean_dataframe(df))
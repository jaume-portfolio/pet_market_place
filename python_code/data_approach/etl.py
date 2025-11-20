from pandasql import sqldf
from python_code.utils.data_loader import ReadCsv


class ExecuteQueryOnDataFrame:
    def __init__(self, df):
        """
        Executes a SQL query on a pandas DataFrame using pandasql. Returns the dataframe result.
        """
        self.dataframe = df
        with open("python_code/data_approach/sql/query.sql", "r") as f:
            query = f.read()
        self.query = query

    def __call__(self):
        # Create a lambda helper
        output = sqldf(self.query, {"df": self.dataframe})
        return output


class ProcessBatchPetMarketPlaceFile:
    def __init__(self):
        """
        Processes the PetMarketPlace CSV data: reads the CSV, transforms it, and outputs a CSV.
        """
        pass

    def _len_distinct_leters(self, s: str):
        letters_list = set([l for l in s if l.isalpha()])
        output = len("".join(letters_list))
        return output

    def __call__(self):
        df = ReadCsv()()
        df["len_sitter_name"] = df["sitter"].apply(self._len_distinct_leters)
        df = ExecuteQueryOnDataFrame(df=df)()
        df = df.sort_values(by=["search_score", "name"], ascending=[False, True])
        df.to_csv("sitters_data_approach.csv", index=False, encoding="utf-8")
        return df

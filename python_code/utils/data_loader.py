import pandas as pd
import os


class ReadCsv:
    def __init__(self, rel_path_file: str = "reviews.csv"):
        """
        Args:
            rel_path_file (str): Path to the csv file (relative to the current working directory).
        """
        if rel_path_file[-4:].lower() != ".csv":
            raise ValueError(
                f"invalid format file: {rel_path_file}. It should be csv file"
            )

        self.abs_path = os.path.abspath(rel_path_file)

        if not os.path.exists(self.abs_path):
            raise ValueError(f"file {self.abs_path} does not exist")

    def __call__(self) -> pd.DataFrame:
        df = pd.read_csv(self.abs_path)
        return df


# ReadCsv(rel_path_file='reviews.csv')()

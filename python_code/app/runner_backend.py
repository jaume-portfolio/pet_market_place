from python_code.utils.data_loader import ReadCsv
from python_code.backend_approach.service.sitter_service import SitterService
from python_code.backend_approach.service.owner_service import OwnerService
from python_code.backend_approach.service.user_service import UserService
from python_code.backend_approach.service.review_service import ReviewService
from python_code.backend_approach.database.database import Database
import pandas as pd


class BackendApproach:
    def __init__(self):
        """
        Backend approach to process PetMarketPlace data.

        Handles creation of Users, Sitters, Owners, and Reviews from CSV data,
        Integrates all this info into the in-memory database
        calculates sitter scores, and outputs the final 'sitters.csv'.
        """
        self.database = Database()
        self.sitter_service = SitterService(db=self.database)
        self.owner_service = OwnerService(db=self.database)
        self.user_service = UserService(db=self.database)
        self.review_service = ReviewService(db=self.database)

    def _create_sitter(self, row):
        # create sitter and users if needed
        user = self.user_service.get_user(email=row["sitter_email"])
        if user is None:
            user = self.user_service.create_user(
                name=row["sitter"],
                phone_number=row["sitter_phone_number"],
                email=row["sitter_email"],
            )

        sitter = self.sitter_service.get_sitter_by_user(user=user)
        if sitter is None:
            sitter = self.sitter_service.create_sitter(user=user)

        return sitter

    def _create_owner(self, row):
        # create owner and user if needed
        user = self.user_service.get_user(email=row["owner_email"])
        if user is None:
            user = self.user_service.create_user(
                name=row["owner"],
                phone_number=row["owner_phone_number"],
                email=row["owner_email"],
            )

        owner = self.owner_service.get_owner_by_user(user=user)
        if owner is None:
            owner = self.owner_service.create_owner(user=user)

        return owner

    def _calculate_scores_and_create_csv(self):
        rows = []
        for sitter in self.database.table_sitters:
            search_score, rating_score = self.sitter_service.calculate_search_score(
                sitter=sitter
            )
            row_dict = {}
            row_dict["email"] = sitter.user.email
            row_dict["name"] = sitter.user.name
            row_dict["profile_score"] = "{:.2f}".format(sitter.profile_score)
            row_dict["ratings_score"] = "{:.2f}".format(rating_score)
            row_dict["search_score"] = "{:.2f}".format(search_score)

            rows.append(row_dict)

            sitters_df = pd.DataFrame(rows)

        sitters_df = sitters_df.sort_values(
            by=["search_score", "name"], ascending=[False, True]
        )
        sitters_df.to_csv("sitters.csv", index=False, encoding="utf-8")

    def __call__(self):
        df = ReadCsv()()

        # integrate all the info into the database
        for index, row in df.iterrows():
            row = dict(row)
            # create sitter
            sitter = self._create_sitter(row)
            # create owner
            owner = self._create_owner(row)
            # create reviews
            self.review_service.create_review(
                sitter=sitter, owner=owner, rating=float(row["rating"])
            )
            # calculate scores and create csv

        # iterate the sitters, calculate the scores and return a csv
        self._calculate_scores_and_create_csv()

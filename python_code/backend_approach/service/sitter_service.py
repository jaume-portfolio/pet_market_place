from python_code.backend_approach.database.database import Database
from python_code.backend_approach.domain.user import User
from python_code.backend_approach.domain.sitter import Sitter


class SitterService:
    def __init__(self, db: Database):
        """
        Service layer for managing Sitter entities.

        Handles creation, retrieval, and calculation of ratings and search scores
        for sitters using the database interface.

        Attributes:
            database (Database): The database interface for storing and retrieving data.
        """
        if not isinstance(db, Database):
            raise ValueError(f"db parameter should be a Database instance")
        self.database = db

    def get_sitter_by_user(self, user: User):
        sitter = self.database.get_sitter_by_user(user)
        return sitter

    def create_sitter(self, user: User):
        sitter = Sitter(user)
        self.database.add_sitter(sitter)
        return sitter

    def calculate_rating_score(self, sitter: Sitter):
        sitter_reviews = self.database.get_review_by_sitter(sitter)
        if len(sitter_reviews) == 0:
            output = None
        else:
            review_counter = len(sitter_reviews)
            sum_rating_reviews = 0
            for review in sitter_reviews:
                sum_rating_reviews = sum_rating_reviews + review.rating

            output = float(sum_rating_reviews) / review_counter

        return output

    def calculate_search_score(self, sitter: Sitter):
        n = 10
        rating_score = self.calculate_rating_score(sitter)
        if rating_score is None:
            return None
        else:
            reviews_counter = len(self.database.get_review_by_sitter(sitter))
            if reviews_counter == 0:
                search_score = sitter.profile_score
            elif reviews_counter >= 10:
                search_score = rating_score
            else:
                search_score = (
                    sitter.profile_score * float(n - reviews_counter)
                ) / 10 + (reviews_counter * rating_score) / 10

        return search_score, rating_score

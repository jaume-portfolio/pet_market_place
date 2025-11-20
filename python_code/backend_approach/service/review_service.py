from python_code.backend_approach.database.database import Database
from python_code.backend_approach.domain.owner import Owner
from python_code.backend_approach.domain.sitter import Sitter
from python_code.backend_approach.domain.review import Review


class ReviewService:
    def __init__(self, db: Database):
        """
        Service layer for managing Review entities.

        Handles creation and persistence of reviews linking sitters and owners,
        ensuring proper validation through domain models.

        Attributes:
            database (Database): The database interface.
        """
        if not isinstance(db, Database):
            raise ValueError(f"db parameter should be a Database instance")
        self.database = db

    def create_review(self, sitter: Sitter, owner: Owner, rating: float):
        review = Review(sitter=sitter, owner=owner, rating=rating)
        self.database.add_review(review=review)

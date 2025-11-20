from python_code.backend_approach.domain.owner import Owner
from python_code.backend_approach.domain.sitter import Sitter


class Review:
    def __init__(self, sitter: Sitter, owner: Owner, rating: float):
        """
        Create a Review object linking an Owner to a Sitter with a rating.

        Args:
            sitter (Sitter): A Sitter instance being reviewed.
            owner (Owner): An Owner instance who wrote the review.
            rating (float): A numeric rating between 0 and 5 inclusive.
        """
        if not isinstance(sitter, Sitter):
            raise ValueError(f"User should be a valid instance of type Sitter")
        if not isinstance(owner, Owner):
            raise ValueError(f"User should be a valid instance of type Owner")
        if not isinstance(rating, float):
            raise ValueError(f"User should be a valid instance of type float")
        if rating > 5 or rating < 0:
            raise ValueError(f"rating should be a valid float between 0 and 5")

        self.sitter = sitter
        self.owner = owner
        self.rating = rating

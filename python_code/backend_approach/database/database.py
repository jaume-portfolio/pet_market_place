from python_code.backend_approach.domain.user import User
from python_code.backend_approach.domain.owner import Owner
from python_code.backend_approach.domain.sitter import Sitter
from python_code.backend_approach.domain.review import Review
from typing import Optional


class Database:
    def __init__(self):
        """
        In-memory database for Users, Sitters, Owners, and Reviews.

        Provides simple add and get operations with basic integrity checks.
        """
        self.table_users = []
        self.table_sitters = []
        self.table_owners = []
        self.table_reviews = []

    def add_user(self, user: User):
        email = user.email
        for existing_user in self.table_users:
            if email == existing_user.email:
                raise ValueError(f"Database Error: the email already exist")

        self.table_users.append(user)

    def get_user_by_email(self, email: str):
        for user in self.table_users:
            if user.email == email:
                return user

        return None

    def add_sitter(self, sitter: Sitter):
        user = sitter.user
        if user not in self.table_users:
            raise ValueError(f"Database Error: the user does nox exist")
        for existing_sitter in self.table_sitters:
            if existing_sitter.user == user:
                raise ValueError(
                    f"Database Error: sitter with the same user already exists"
                )

        self.table_sitters.append(sitter)

    def get_sitter_by_user(self, user: User):
        for sitter in self.table_sitters:
            if sitter.user == user:
                return sitter

        return None

    def add_owner(self, owner: Owner):
        user = owner.user
        if user not in self.table_users:
            raise ValueError(f"Database Error: the user does nox exist")
        for existing_owner in self.table_owners:
            if existing_owner.user == user:
                raise ValueError(
                    f"Database Error: owner with the same user already exists"
                )

        self.table_owners.append(owner)

    def get_owner_by_user(self, user: User):
        for owner in self.table_owners:
            if owner.user == user:
                return owner

        return None

    def add_review(self, review: Review):
        if review.owner not in self.table_owners:
            raise ValueError(f"Database Error: owner not in database")

        if review.sitter not in self.table_sitters:
            raise ValueError(f"Database Error: sitter not in database")

        self.table_reviews.append(review)

    def get_review_by_sitter(self, sitter: Sitter):
        sitter_reviews = []
        for review in self.table_reviews:
            if review.sitter == sitter:
                sitter_reviews.append(review)

        return sitter_reviews

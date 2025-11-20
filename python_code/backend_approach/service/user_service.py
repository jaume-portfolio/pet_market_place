from python_code.backend_approach.database.database import Database
from python_code.backend_approach.domain.user import User


class UserService:
    def __init__(self, db: Database):
        """
        Service layer for managing User entities.

        Handles creation and retrieval of users from the database,
        including basic validation of email format and user data.

        Attributes:
            database (Database): The database interface for storing and retrieving users.
        """
        if not isinstance(db, Database):
            raise ValueError(f"db parameter should be a Database instance")
        self.database = db

    def get_user(self, email: str):
        if "@" not in email:
            raise ValueError(
                f"Invalid format for email. It sould contain the character @"
            )
        user = self.database.get_user_by_email(email)
        return user

    def create_user(self, name: str, phone_number: str, email: str):
        user = User(name=name, phone_number=str(phone_number), email=email)
        self.database.add_user(user=user)
        return user

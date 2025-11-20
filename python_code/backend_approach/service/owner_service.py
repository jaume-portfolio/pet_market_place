from python_code.backend_approach.database.database import Database
from python_code.backend_approach.domain.user import User
from python_code.backend_approach.domain.owner import Owner


class OwnerService:
    def __init__(self, db: Database):
        """
        Service layer for managing Owner entities.

        Handles creation and retrieval of owners from the database
        using associated User instances.

        Attributes:
            database (Database): The database interface.
        """
        if not isinstance(db, Database):
            raise ValueError(f"db parameter should be a Database instance")
        self.database = db

    def get_owner_by_user(self, user: User):
        owner = self.database.get_owner_by_user(user)
        return owner

    def create_owner(self, user: User):
        owner = Owner(user)
        self.database.add_owner(owner)
        return owner

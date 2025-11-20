from python_code.backend_approach.domain.user import User


class Owner:
    def __init__(self, user: User):
        """
        Create an Owner object linked to a User.

        Args:
            user (User): A valid User instance representing the owner.
        """
        if not isinstance(user, User):
            raise ValueError(f"User should be a valid instance of type User")
        self.user = user

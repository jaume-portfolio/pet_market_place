from python_code.backend_approach.domain.user import User


class Sitter:
    def __init__(self, user: User):
        """
        Create a Sitter object linked to a User.
        Args:
            user (User): A valid User instance representing the sitter.
        """
        if not isinstance(user, User):
            raise ValueError(f"User should be a valid instance of type User")
        self.user = user
        self.profile_score = self._calculate_sitter_profile_score()

    def _calculate_sitter_profile_score(self):
        number_letters_alphabet = 26
        letters_list = set([letter for letter in self.user.name if letter.isalpha()])
        length = len("".join(letters_list))
        output = (float(length) / number_letters_alphabet) * 5
        return output

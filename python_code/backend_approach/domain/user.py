class User:
    def __init__(self, name: str, phone_number: str, email: str):
        """
        Create a User object with validated name, phone number, and email.

        Args:
            name (str): The full name of the user. Max 50 characters.
            phone_number (str): Phone number in the format '+34111222333'.
            email (str): Email address containing '@'.

        """
        parameters = {"name": name, "phone_number": phone_number, "email": email}

        # validate instances
        for parameter_name, parameter_value in parameters.items():
            if not isinstance(parameter_value, str):
                raise ValueError(
                    f"Parameter {parameter_name} should be of type str. Not type {type(parameter_value)}"
                )

        # validate name
        if len(name) > 50:
            raise ValueError(f"The length the name should be shorter than 50")

        # validate phone_number
        if len(phone_number) != 11 or not phone_number.isdigit():
            raise ValueError(
                f"Invalid format for phone number. It should be Ex: +34111222333"
            )

        # validate email
        if "@" not in email:
            raise ValueError(
                f"Invalid format for email. It sould contain the character @"
            )

        # assign atributes
        self.name = name
        self.phone_number = phone_number
        self.email = email

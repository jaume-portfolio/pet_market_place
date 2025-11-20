import pytest
from python_code.backend_approach.domain.user import User


def test_valid_user():
    """Checks user has right parameters"""
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    assert user.name == "Jaume"
    assert user.phone_number == "99111222333"
    assert user.email == "jaume@gmail.com"


def test_valid_user_name_length():
    """Checks it raises errors when invalid name length"""
    with pytest.raises(ValueError):
        User(
            "dsvfdfncskjdhfnwldsivjnildjfcmwdlfjmlsdijvsldvjsvcsfv",
            "99111222333",
            "jaume@gmail.com",
        )


def test_valid_user_phone_number():
    """Checks it raises errors when ninvalid phone number"""
    with pytest.raises(ValueError):
        User("Jaume", "AGDJDJ", "jaume@gmail.com")


def test_valid_user_email():
    """Checks it raises errors when invalid email"""
    with pytest.raises(ValueError):
        User("Jaume", "99111222333", "jaumegmail.com")

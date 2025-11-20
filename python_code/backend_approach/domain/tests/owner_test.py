import pytest
from python_code.backend_approach.domain.owner import Owner
from python_code.backend_approach.domain.user import User


def test_valid_owner():
    """Checks owner has right parameters"""
    owner = Owner(user=User("Jaume", "99111222333", "jaume@gmail.com"))
    assert owner.user.name == "Jaume"
    assert owner.user.phone_number == "99111222333"
    assert owner.user.email == "jaume@gmail.com"


def test_valid_owner_user():
    """Checks it raises errors when invalid user"""
    with pytest.raises(ValueError):
        Owner(user="Jaume")

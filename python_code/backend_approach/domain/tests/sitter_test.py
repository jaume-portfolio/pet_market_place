import pytest
from python_code.backend_approach.domain.sitter import Sitter
from python_code.backend_approach.domain.user import User


def test_valid_sitter():
    """Checks sitter has right parameters"""
    sitter = Sitter(user=User("Jaume", "99111222333", "jaume@gmail.com"))
    assert sitter.user.name == "Jaume"
    assert sitter.user.phone_number == "99111222333"
    assert sitter.user.email == "jaume@gmail.com"


def test_valid_sitter_user():
    """Checks it raises errors when invalid user"""
    with pytest.raises(ValueError):
        Sitter(user="Jaume")


def test_valid_sitter_profile_score():
    """Checks sitter has right parameters"""
    sitter = Sitter(user=User("Jaume", "99111222333", "jaume@gmail.com"))
    assert sitter.profile_score == (5 / 26) * 5

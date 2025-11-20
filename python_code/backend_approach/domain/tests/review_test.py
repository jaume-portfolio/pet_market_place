import pytest
from python_code.backend_approach.domain.owner import Owner
from python_code.backend_approach.domain.sitter import Sitter
from python_code.backend_approach.domain.user import User
from python_code.backend_approach.domain.review import Review


def test_valid_review():
    """Checks review has right parameters"""
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    owner = Owner(user=user)
    sitter = Sitter(user=user)
    review = Review(sitter=sitter, owner=owner, rating=float(2))
    assert review.owner == owner
    assert review.sitter == sitter
    assert review.rating == float(2)


def test_valid_review_owner():
    """Checks it raises errors when invalid owner"""
    with pytest.raises(ValueError):
        user = User("Jaume", "99111222333", "jaume@gmail.com")
        sitter = Sitter(user=user)
        Review(sitter=sitter, owner="Jaume", rating=float(2))


def test_valid_review_sitter():
    """Checks it raises errors when invalid sitter"""
    with pytest.raises(ValueError):
        user = User("Jaume", "99111222333", "jaume@gmail.com")
        owner = Owner(user=user)
        Review(sitter="Jaume", owner=owner, rating=float(2))


def test_valid_review_rating():
    """Checks it raises errors when invalid rating"""
    with pytest.raises(ValueError):
        user = User("Jaume", "99111222333", "jaume@gmail.com")
        owner = Owner(user=user)
        sitter = Sitter(user=user)
        Review(sitter=sitter, owner=owner, rating=float(10))

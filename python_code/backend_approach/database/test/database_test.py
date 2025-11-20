import pytest
from python_code.backend_approach.domain.user import User
from python_code.backend_approach.domain.owner import Owner
from python_code.backend_approach.domain.sitter import Sitter
from python_code.backend_approach.domain.review import Review
from python_code.backend_approach.database.database import Database


# users
def test_add_user_success():
    db = Database()
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    db.add_user(user)
    assert user in db.table_users


def test_add_user_duplicate_raises():
    db = Database()
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    db.add_user(user)
    with pytest.raises(ValueError):
        db.add_user(user)


# sitters
def test_add_sitter_success():
    db = Database()
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    db.add_user(user)
    sitter = Sitter(user)
    db.add_sitter(sitter)
    assert sitter in db.table_sitters


def test_add_sitter_without_user_raises():
    db = Database()
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    sitter = Sitter(user)
    with pytest.raises(ValueError):
        db.add_sitter(sitter)


# owners


def test_add_owner_success():
    db = Database()
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    db.add_user(user)
    owner = Owner(user)
    db.add_owner(owner)
    assert owner in db.table_owners


def test_add_owner_without_user_raises():
    db = Database()
    user = User("Jaume", "99111222333", "jaume@gmail.com")
    owner = Owner(user)
    with pytest.raises(ValueError):
        db.add_owner(owner)


# reviews


def test_add_review_success():
    db = Database()
    user1 = User("Jaume", "99111222333", "jaume@gmail.com")
    user2 = User("Michael", "99111222333", "michael@gmail.com")
    db.add_user(user1)
    db.add_user(user2)
    sitter = Sitter(user1)
    owner = Owner(user2)
    db.add_sitter(sitter)
    db.add_owner(owner)
    review = Review(sitter, owner, 4.5)
    db.add_review(review)
    assert review in db.table_reviews

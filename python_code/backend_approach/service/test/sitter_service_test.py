import pytest
from python_code.backend_approach.database.database import Database
from python_code.backend_approach.service.sitter_service import SitterService
from python_code.backend_approach.service.owner_service import OwnerService
from python_code.backend_approach.service.review_service import ReviewService
from python_code.backend_approach.service.user_service import UserService
from python_code.backend_approach.domain.user import User
from python_code.backend_approach.domain.sitter import Sitter
from python_code.backend_approach.domain.owner import Owner
from python_code.backend_approach.domain.review import Review


def test_create_sitter():
    db = Database()
    sitter_service = SitterService(db)
    user_service = UserService(db)
    user = user_service.create_user("Jaume", "99111222333", "jaume@gmail.com")

    sitter = sitter_service.create_sitter(user)
    assert isinstance(sitter, Sitter)
    assert sitter in db.table_sitters


def test_rating_seach_score():
    # create database and create two users and one sitter and one owner
    db = Database()
    sitter_service = SitterService(db)
    owner_service = OwnerService(db)
    review_service = ReviewService(db)
    user_service = UserService(db)

    sitter_user = user_service.create_user(
        "Leilani R.", "99111222333", "jaume@gmail.com"
    )
    sitter = sitter_service.create_sitter(sitter_user)
    owner_user = user_service.create_user("Owner", "99988877766", "owner@gmail.com")
    owner = owner_service.create_owner(owner_user)

    # 2 review
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    search_score, rating = sitter_service.calculate_search_score(sitter)
    expected = (sitter.profile_score * 8) / 10 + (2 * 5.0) / 10
    assert rating == 5.0
    assert search_score == expected

    # 5 review
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    search_score, rating = sitter_service.calculate_search_score(sitter)
    expected = (sitter.profile_score * 5) / 10 + (5 * 5.0) / 10
    assert rating == 5.0
    assert search_score == expected

    # 10 review
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    review_service.create_review(sitter=sitter, owner=owner, rating=5.0)
    search_score, rating = sitter_service.calculate_search_score(sitter)
    expected = rating
    assert rating == 5.0
    assert search_score == rating

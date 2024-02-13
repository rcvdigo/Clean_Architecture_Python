from src.infra.db.repositories.users_repositories import UsersRepository
from .user_finder import UserFinder


def test_find():
    user_finder = UserFinder(users_repository=UsersRepository())
    
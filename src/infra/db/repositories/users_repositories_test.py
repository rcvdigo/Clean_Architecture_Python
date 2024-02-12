# from src.infra.db.settings.connection import DbConnectionHandler
from .users_repositories import UsersRepository


def test_insert_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 34

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

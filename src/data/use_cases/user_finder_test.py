# from src.infra.db.repositories.users_repositories import UsersRepository
from typing import List
from src.domain.models.users import Users
from src.infra.db.tests.users_repository import UsersRepositorySpy as UsersRepository
from .user_finder import UserFinder


def test_find():
    first_name = 'Rodrigo'

    repo = UsersRepository()
    user_finder = UserFinder(users_repository=repo)
    
    response = user_finder.find(first_name=first_name)

    # print(f"\n\n{response}\n\n")

    # print(f"\n\n{repo.select_user_attributes}\n\n")

    assert repo.select_user_attributes["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    first_name = 'Rodrigo123'

    repo = UsersRepository()
    user_finder = UserFinder(users_repository=repo)
    
    try:
        user_finder.find(first_name=first_name)
        assert False
    except Exception as ex:
        assert(str(ex)) == "Nome inválido para busca"

def test_find_error_name_too_long():
    first_name = 'RodrigoRodrigoRodrigoRodrigoRodrigoRodrigo'

    repo = UsersRepository()
    user_finder = UserFinder(users_repository=repo)

    try:
        user_finder.find(first_name=first_name)
        assert False
    except Exception as ex:
        assert(str(ex)) == "Nome muito grande para busca, o máximo de caracteres é 18"

def test_find_error_user_not_found():
    class UsersRepositoryError(UsersRepository):
        def select_user(self, first_name: str):
            return []
        
    first_name = 'Rodrigo'

    repo = UsersRepositoryError()
    user_finder = UserFinder(users_repository=repo)

    try:
        user_finder.find(first_name=first_name)
        assert False
    except Exception as ex:
        assert(str(ex)) == "Usuário não existe na base de dados!"

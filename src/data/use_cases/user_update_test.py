import json
from src.infra.db.repositories.users_repositories import UsersRepository
# from src.infra.db.tests.users_repository import UsersRepositorySpy as UsersRepository
from .user_update import UserUpdate


def test_update_user():
    user_id = 53
    first_name = input("\nDigite um nome: \n")
    last_name = input("\nDigite um sobre nome: \n")
    age = int(input("\nDigite uma idade: \n"))

    repo = UsersRepository()
    user_register = UserUpdate(users_repository=repo)

    response = user_register.update_user(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        age=age
        )

    print(json.dumps(response, indent=1))

    # assert response["type"]  == "Users"
    # assert response["count"]  == 1
    # assert response["attributes"] != []
    # assert repo.update_user_attributes["user_id"]  == user_id
    # assert repo.update_user_attributes["first_name"]  == first_name
    # assert repo.update_user_attributes["last_name"]  == last_name
    # assert repo.update_user_attributes["age"]  == age

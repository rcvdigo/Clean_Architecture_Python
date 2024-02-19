import json
from src.infra.db.tests.users_repository import UsersRepositorySpy as UsersRepository
from .user_register import UserRegister


def test_register():
    first_name = 'Rodrigo'
    last_name = 'Camurca'
    age = 29

    repo = UsersRepository()
    user_register = UserRegister(users_repository=repo)
    
    response = user_register.register(
        first_name=first_name,
        last_name=last_name,
        age=age
     )
    
    print(json.dumps(response, indent=1))

    assert response["type"]  == "Users"
    assert response["count"]  == 1
    assert response["attributes"] != []
    assert repo.insert_user_attributes["first_name"]  == first_name
    assert repo.insert_user_attributes["last_name"]  == last_name
    assert repo.insert_user_attributes["age"]  == age

def test_register_first_name_error():
    first_name = 'Rodrigo12314'
    last_name = 'Camurca'
    age = 29

    repo = UsersRepository()
    user_register = UserRegister(users_repository=repo)

    try:
        user_register.register(
            first_name,
            last_name,
            age
        )
        assert False
    except Exception as ex:
        assert str(ex) == "Nome inválido o cadastro"

from typing import Dict
from src.domain.use_cases.user_register import UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserRegister(UserRegisterInterface):
    
    def __init__(
            self,
            users_repository: UsersRepositoryInterface
            ) -> Dict:
        
        self.__users_repository = users_repository

    def register(
        self,
        first_name: str,
        last_name: str,
        age: int
        ) -> Dict:
        
        self.__validate_name(first_name=first_name)
        self.__validate_name(first_name=last_name)
        self.__registry_user_informations(
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        response = self.__format_response(
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        return response
    
    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        # Caso first_name não seja as letras do alfabeto
        if not first_name.isalpha():
            raise Exception(
                'Nome inválido para busca'
                )
        
        if len(first_name) > 18:
            raise Exception(
                'Nome muito grande para busca, o máximo de caracteres é 18'
                )

    def __registry_user_informations(
        self,
        first_name: str,
        last_name: str,
        age: int
        ) -> None:
        
        self.__users_repository.insert_user(
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        
    @classmethod
    def __format_response(
        cls,
        first_name: str,
        last_name: str,
        age: int
    ) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            }
        }
        return response

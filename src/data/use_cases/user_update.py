from typing import Dict
from src.domain.use_cases.user_update import UserUpdateInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types import HttpBadRequestError


class UserUpdate(UserUpdateInterface):
    
    def __init__(
            self,
            users_repository: UsersRepositoryInterface
            ) -> Dict:
        
        self.__users_repository = users_repository
        
    def update_user(
            self,
            user_id: int,
            first_name: str,
            last_name: str,
            age: int
            ) -> Dict:

            self.__validate_name(first_name=first_name)
            
            self.__update_users_infomations(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                age=age
            )

            response = self.__format_response(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                age=age
            )
            return response


    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        # Caso first_name não seja as letras do alfabeto
        if not first_name.isalpha():
            raise HttpBadRequestError(
                'Nome inválido para busca'
                )
        
        if len(first_name) > 18:
            raise HttpBadRequestError(
                'Nome muito grande para busca, o máximo de caracteres é 18'
                )
        
    @classmethod
    def __format_response(
        cls,
        user_id: int,
        first_name: str,
        last_name: str,
        age: int
    ) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "id": user_id,
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            }
        }
        return response

    def __update_users_infomations(
            self,
            user_id: int,
            first_name: str,
            last_name: str,
            age: int
            ) -> None:

            self.__users_repository.update_user(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                age=age
                )

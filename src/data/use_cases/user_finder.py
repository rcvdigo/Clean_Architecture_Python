from typing import Dict
from typing import List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpBadRequestError
from src.errors.types import HttpNotFoundError


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict: 
        self.__validate_name(first_name=first_name)
        users = self.__search_user(first_name=first_name)
        response = self.__format_response(users=users)
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

    def __search_user(self, first_name: str) -> List[Users]:
        query = self.__users_repository.select_user(first_name=first_name)
        if query == []:
            raise HttpNotFoundError('Usuário não existe na base de dados!')
        return query
    
    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []

        for user in users:
            attributes.append(
                {
                    "first_name": user.first_name,
                    "age": user.age
                }
            )

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
        return response

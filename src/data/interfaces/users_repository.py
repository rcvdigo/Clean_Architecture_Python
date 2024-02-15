from abc import ABC
from abc import abstractmethod
from typing import List
from src.domain.models.users import Users


class UsersRepositoryInterface(ABC):
    
    @classmethod # Nos parametros os ": type-hitss" é como se fosse um tipo de comentário, ex docstring
    def insert_user(
        self,
        first_name: str,
        last_name: str,
        age: int
    ) -> None: pass


    @classmethod
    def select_user(
        self,
        first_name: str
    ) -> List[Users]: pass

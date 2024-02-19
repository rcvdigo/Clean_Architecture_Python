from abc import ABC
from abc import abstractmethod
from typing import Dict


class UserUpdateInterface(ABC):

    @abstractmethod
    def update_user(
        self, 
        user_id: int,
        first_name: str,
        last_name: str,
        age: int
        ) -> Dict: 
        pass

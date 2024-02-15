from abc import ABC
from abc import abstractmethod
from typing import Dict


class UserRegisterInterface(ABC):
    
    @abstractmethod
    def register(
        self,
        first_name: str,
        last_name: str,
        age: int
        ) -> Dict:
        pass
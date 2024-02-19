from typing import List
from src.domain.models.users import Users


class UsersRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}
        self.update_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age
        return
    
    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes["first_name"] = first_name
        return[
            Users(1, first_name, 'last', 28),
            Users(2, first_name, 'last_2', 29)
        ]

    def update_user(
            self,
            user_id: int,
            first_name: str,
            last_name: str,
            age: int    
        ):
        self.update_user_attributes["user_id"] = user_id
        self.update_user_attributes["first_name"] = first_name
        self.update_user_attributes["last_name"] = last_name
        self.update_user_attributes["age"] = age

        user = Users(user_id, 'first_name', 'last', 25)
        
        user.first_name = first_name
        user.last_name = last_name
        user.age = age
        return user
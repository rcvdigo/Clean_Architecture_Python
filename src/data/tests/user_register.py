from typing import Dict


class UserFinderSpy:
    
    def __init__(self) -> None:
        self.insert_user_attributes = {}

    def register(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age
       
        return {
            "type": "Users",
            "count": 1,
            "attributes": [
                {
                    "first_name": self.insert_user_attributes["first_name"],
                    "last_name": self.insert_user_attributes["last_name"],
                    "age": self.insert_user_attributes["age"],
                }
            ]
        }

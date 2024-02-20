from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_update_validator(request: any):
    body_validator = Validator(
        {
            "id": {
                "type": "integer",
                "required": True,
                "empty": False
            },
            "first_name": {
                "type": "string",
                "required": True,
                "empty": False
            },
            "last_name": {
                "type": "string",
                "required": True,
                "empty": False
            },
            "age": {
                "type": "integer",
                "required": True,
                "empty": False
            }
        }
    )

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(message=body_validator.errors)
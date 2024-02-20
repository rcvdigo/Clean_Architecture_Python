from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_find_validator(request: any):
    body_validator = Validator(
        {
            "first_name": {
                "type": "string",
                "required": True,
                "empty": False
            }
        }
    )

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(message=body_validator.errors)
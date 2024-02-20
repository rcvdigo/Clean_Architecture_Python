from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_find_validator(request: any):
    query_params_validator = Validator(
        {
            "first_name": {
                "type": "string",
                "required": True,
                "empty": False
            }
        }
    )

    response = query_params_validator.validate(request.args)

    if response is False:
        raise HttpUnprocessableEntityError(message=query_params_validator.errors)

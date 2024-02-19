import json
from src.presentation.http_types.http_response import HttpResponse
from src.data.tests.user_register import UserFinderSpy as UserRegister
from .user_register_controller import UserRegisterController


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "first_name": "meuTeste",
            "last_name": "last_teste",
            "age": 29
            }

def test_handle():
    http_request_mock =  HttpRequestMock()
    use_case = UserRegister()
    user_register_controller = UserRegisterController(use_case=use_case)

    response = user_register_controller.handle(http_request=http_request_mock)

    print(f"\n\n{response}\n\n")
    print(f"\n{json.dumps(response.body, indent=1)}\n")
    print(f"\n{response.status_code}\n")

    assert isinstance(response, HttpResponse)


import json
from src.presentation.http_types.http_response import HttpResponse
from src.data.tests.user_finder import UserFinderSpy as UserFinder
from .user_finder_controller import UserFinderController


class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"first_name": "meuTeste"}

def test_handle():
    http_request_mock =  HttpRequestMock()
    use_case = UserFinder()
    user_finder_controller = UserFinderController(use_case=use_case)

    response = user_finder_controller.handle(http_request=http_request_mock)

    print(f"\n\n{response}\n\n")
    print(f"\n{json.dumps(response.body, indent=1)}\n")
    print(f"\n{response.status_code}\n")

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None

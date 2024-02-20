from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_update import UserUpdateInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserUpdateController(ControllerInterface):

    def __init__(self, use_case: UserUpdateInterface) -> None:
        self.__use_case = use_case

    def handle(
            self,
            http_request: HttpRequest) -> HttpResponse:

            user_id = http_request.body["id"]
            first_name = http_request.body["first_name"]
            last_name = http_request.body["last_name"]
            age = http_request.body["age"]

            response = self.__use_case.update_user(
                 user_id=user_id,
                 first_name=first_name,
                 last_name=last_name,
                 age=age
            )

            return HttpResponse(
                 status_code=200,
                 body={"data": response}
            )

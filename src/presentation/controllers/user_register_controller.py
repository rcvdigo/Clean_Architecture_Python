from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_register import UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserRegisterController(ControllerInterface):
    
    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__use_case = use_case

    
    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        first_name = http_request.body["first_name"]
        last_name = http_request.body["last_name"]
        age = http_request.body["age"]

        response = self.__use_case.register(
            first_name=first_name,
            last_name=last_name,
            age=age
            )

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )

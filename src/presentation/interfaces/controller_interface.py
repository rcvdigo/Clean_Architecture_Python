from abc import ABC
from abc import abstractmethod
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):
    
    @abstractmethod
    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse: pass

from src.presentation.http_types.http_response import HttpResponse
from .types import HttpNotFoundError
from .types import HttpBadRequestError


def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": {
                    "title": error.name,
                    "detail": error.message
                }
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": {
                "title": "Generic Error, contact your administrator",
                "detail": str(error)
            }
        }
    )

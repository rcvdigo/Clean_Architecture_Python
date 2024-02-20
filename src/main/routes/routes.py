from flask import Blueprint
from flask import request as request_flask
from flask import jsonify


# Import from adapters
from src.main.adapters.request_adapter import request_adapter

# Import from composers
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

# Import error handler
from src.errors.error_handler import handler_errors

# Import Validators
from src.validators.user_register_validator import user_register_validator
from src.validators.user_find_validator import user_find_validator


user_route_bp = Blueprint("user_routes", __name__) # Apelidando o @app para @user_route_bp

@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = None
    try:
        # Protegendo a inserção de dados injetando o validator user_register_validator
        user_find_validator(request=request_flask)

        http_response = request_adapter(
            request=request_flask,
            controller=user_finder_composer()
        )
    except Exception as exeception:
        http_response = handler_errors(error=exeception)

    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/user", methods=["POST"])
def register_user():
    http_response = None
    try:
        # Protegendo a inserção de dados injetando o validator user_register_validator
        user_register_validator(request=request_flask)

        http_response = request_adapter(
            request=request_flask,
            controller=user_register_composer()
            )
    except Exception as exeception:
        http_response = handler_errors(error=exeception)
        
    return jsonify(http_response.body), http_response.status_code

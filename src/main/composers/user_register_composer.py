from src.infra.db.repositories.users_repositories import UsersRepository
from src.data.use_cases.user_register import UserRegister
from src.presentation.controllers.user_register_controller import UserRegisterController


def user_register_composer():
    repository = UsersRepository()
    use_case = UserRegister(users_repository=repository)
    controller = UserRegisterController(use_case=use_case)

    return controller.handle

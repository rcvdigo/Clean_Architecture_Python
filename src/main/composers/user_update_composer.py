from src.infra.db.repositories.users_repositories import UsersRepository
from src.data.use_cases.user_update import UserUpdate
from src.presentation.controllers.user_update_controller import UserUpdateController


def user_update_composer():
    repository = UsersRepository()
    use_case = UserUpdate(users_repository=repository)
    controller = UserUpdateController(use_case=use_case)

    return controller.handle

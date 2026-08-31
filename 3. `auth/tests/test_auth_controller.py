from auth.controller.auth_controller import AuthController
from auth.service.auth_service import AuthService
from auth.repository.auth_repository import AuthRepository

def test_handle_login():
    repo = AuthRepository()
    service = AuthService(repo)
    controller = AuthController(service)
    # Ajoutez des tests pour la méthode handle_login
    pass

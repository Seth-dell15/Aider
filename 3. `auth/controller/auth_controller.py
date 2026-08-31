from .auth_service import AuthService

class AuthController:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def handle_login(self, username, password):
        return self.auth_service.authenticate_user(username, password)

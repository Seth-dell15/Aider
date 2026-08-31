from .auth_repository import AuthRepository

class AuthService:
    def __init__(self, auth_repository):
        self.auth_repository = auth_repository

    def authenticate_user(self, username, password):
        return self.auth_repository.authenticate(username, password)

from auth.service.auth_service import AuthService
from auth.repository.auth_repository import AuthRepository

def test_authenticate_user():
    repo = AuthRepository()
    service = AuthService(repo)
    # Ajoutez des tests pour la méthode authenticate_user
    pass

from .auth_repository import AuthRepository

class AuthService:
    """
    Classe responsable de la logique métier liée à l'authentification.
    """

    def __init__(self, auth_repository):
        """
        Constructeur de la classe AuthService.

        :param auth_repository: Instance de AuthRepository
        """
        self.auth_repository = auth_repository

    def authenticate_user(self, username, password):
        """
        Méthode pour authentifier un utilisateur.

        :param username: Nom d'utilisateur
        :param password: Mot de passe
        :return: True si l'utilisateur est authentifié, False sinon
        """
        return self.auth_repository.authenticate(username, password)

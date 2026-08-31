from .auth_service import AuthService

class AuthController:
    """
    Classe responsable de la gestion des requêtes d'authentification.
    """

    def __init__(self, auth_service):
        """
        Constructeur de la classe AuthController.

        :param auth_service: Instance de AuthService
        """
        self.auth_service = auth_service

    def handle_login(self, username, password):
        """
        Méthode pour gérer la requête de login.

        :param username: Nom d'utilisateur
        :param password: Mot de passe
        :return: Résultat de l'authentification
        """
        return self.auth_service.authenticate_user(username, password)

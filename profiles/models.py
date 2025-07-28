from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente un profil utilisateur, lié à un utilisateur Django.

    Attributs :
        user (User) : L'utilisateur lié au profil.
        favorite_city (str) : Ville préférée (optionnelle).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne une représentation textuelle du profil (le nom d'utilisateur).
        """
        return self.user.username

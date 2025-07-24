from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # L'utilisateur associé à ce profil
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # La ville préférée de l'utilisateur (champ optionnel)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        # Affiche le nom d'utilisateur dans l'interface admin
        return self.user.username

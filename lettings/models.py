from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse postale.

    Attributs :
        number (int): Numéro de rue (1 à 9999).
        street (str): Nom de la rue.
        city (str): Ville.
        state (str): Code de l’état (2 lettres).
        zip_code (int): Code postal (5 chiffres).
        country_iso_code (str): Code ISO du pays (3 lettres).
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Retourne une représentation lisible de l'adresse.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Représente un logement disponible à la location.

    Attributs :
        title (str): Titre du logement.
        address (Address): Adresse liée au logement.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne le titre du logement.
        """
        return self.title

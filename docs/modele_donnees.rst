Modèles et base de données
===========================

Modèles principaux :

- Letting :
  - title (str) : Nom du logement
  - address (ForeignKey → Address) : Lien vers l'adresse associée

- Address :
  - number (Int) : Numéro de rue
  - street (str) : Nom de la rue
  - city (str) : Ville
  - state (str) : État ou région
  - zip_code (str) : Code postal
  - country_iso_code (str) : Code pays ISO (ex. "FRA")

- Profile :
  - user (ForeignKey à User) : Utilisateur lié
  - favorite_city (str) : Ville préférée de l’utilisateur

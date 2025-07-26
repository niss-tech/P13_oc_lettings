# Image de base avec Python 3.11
FROM python:3.11-slim

# Chemin du dossier
WORKDIR /app

# Copie de tous les fichiers du projet dans le conteneur
COPY . /app

# Installation de pip + dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collecte des fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposition du port
EXPOSE 8000

# Démarre le serveur avec gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    # Création de données pour le test
    user = User.objects.create(username="nisrine")
    Profile.objects.create(user=user, favorite_city="Paris")

    # "reverse" permet d'appeler la vue via son nom d’URL
    url = reverse('profiles:index')
    response = client.get(url)

    # Vérification du code de retour 200
    assert response.status_code == 200

    # Vérifie que le bon template est utilisé
    assert 'profiles/index.html' in [t.name for t in response.templates]

    # Vérifie que le nom d'utilisateur apparaît dans le contenu HTML
    assert user.username.encode() in response.content


@pytest.mark.django_db
def test_profile_not_found(client):
    url = reverse('profiles:profile', kwargs={'username': 'utilisateur-inconnu'})
    response = client.get(url)

    # Vérifie que l'on obtient bien une erreur 404
    assert response.status_code == 404

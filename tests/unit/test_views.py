import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_profiles_index_view(client):
    # Création de données pour le test
    user = User.objects.create(username="nisrine")
    Profile.objects.create(user=user, favorite_city="Paris")

    # "reverse" permet d'appeler la vue via son nom d’URL
    url = reverse('profiles_index')
    response = client.get(url)

    # Vérification du code de retour 200
    assert response.status_code == 200

    # Vérifie que le bon template est utilisé
    assert 'profiles/profiles_index.html' in [t.name for t in response.templates]

    # Vérifie que le nom d'utilisateur apparaît dans le contenu HTML
    assert user.username.encode() in response.content


@pytest.mark.django_db
def test_lettings_index_view(client):
    # Création des données de test
    address = Address.objects.create(
        number=123,
        street="Rue de l'Océan",
        city="Nice",
        state="CA",
        zip_code="06000",
        country_iso_code="FRA"
    )
    
    letting = Letting.objects.create(title="Maison test", address=address)

    # Appel de la vue
    url = reverse('lettings_index')
    response = client.get(url)

    # Vérifie que la réponse est bien 200 OK
    assert response.status_code == 200

    # Vérifie que le bon template est utilisé
    assert 'lettings/lettings_index.html' in [t.name for t in response.templates]

    # Vérifie que le titre du logement est dans le contenu HTML
    assert letting.title.encode() in response.content


@pytest.mark.django_db
def test_profile_not_found(client):
    url = reverse('profile', kwargs={'username': 'utilisateur-inconnu'})
    response = client.get(url)

    # Vérifie que l'on obtient bien une erreur 404
    assert response.status_code == 404


@pytest.mark.django_db
def test_letting_not_found(client):
    # Appel avec un ID qui n'existe pas
    url = reverse('letting', kwargs={'letting_id': 9999})
    response = client.get(url)

    # Vérifie que le code retourné est bien une erreur 404
    assert response.status_code == 404

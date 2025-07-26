import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_user_profile_flow(client):
    # Création d'un utilisateur et profil
    user = User.objects.create(username="nissrine")
    Profile.objects.create(user=user, favorite_city="Toulouse")

    # Accès à la page /profiles/ qui vérifie que l'utilisateur est présent
    list_url = reverse('profiles_index')
    response_list = client.get(list_url)
    assert response_list.status_code == 200
    assert user.username.encode() in response_list.content

    # Accès au détails du profil via /profiles/<username>/
    detail_url = reverse('profile', kwargs={'username': user.username})
    response_detail = client.get(detail_url)
    assert response_detail.status_code == 200
    assert b"Toulouse" in response_detail.content

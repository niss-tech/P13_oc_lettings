import pytest
from django.contrib.auth.models import User
from profiles.models import Profile
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create(username="nisrine")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert str(profile) == "nisrine"


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=12, street="Rue du Code", city="Paris", state="FR",
        zip_code="75000", country_iso_code="FR"
    )
    letting = Letting.objects.create(title="Mon Letting", address=address)
    assert str(letting) == "Mon Letting"

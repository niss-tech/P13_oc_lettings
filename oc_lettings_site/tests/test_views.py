from django.urls import reverse


def test_homepage_view(client):
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200
    assert b"Welcome" in response.content

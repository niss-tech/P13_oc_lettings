from django.shortcuts import render
from django.http import HttpResponseNotFound


def index(request):
    # Affiche la page d’accueil principale du site
    return render(request, 'index.html')

# Vue de test temporaire pour afficher la page d'erreur 404 personnalisée
def test_404(request):
    return HttpResponseNotFound(render(request, '404.html'))

# Vue de test temporaire pour déclencher une erreur 500
def test_500(request):
    1 / 0  # crash volontaire


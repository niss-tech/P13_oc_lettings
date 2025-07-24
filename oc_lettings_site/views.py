from django.shortcuts import render


def index(request):
    # Affiche la page d’accueil principale du site
    return render(request, 'index.html')

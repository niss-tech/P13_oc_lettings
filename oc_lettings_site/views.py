from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Vue de la page d’accueil principale du site.

    Affiche simplement le template 'index.html'.

    Args:
        request (HttpRequest): La requête HTTP.

    Returns:
        HttpResponse: La page d’accueil du site.
    """
    logger.info("Page d’accueil principale affichée.")
    return render(request, 'index.html')


# from django.http import HttpResponseNotFound
# Vue de test temporaire pour afficher la page d'erreur 404 personnalisée
# def test_404(request):
#     return HttpResponseNotFound(render(request, '404.html'))


# Vue de test temporaire pour déclencher une erreur 500
# def test_500(request):
#     1 / 0  # crash volontaire

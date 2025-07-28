from django.shortcuts import render, get_object_or_404
from lettings.models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Vue de la page d'accueil des lettings.

    Affiche la liste des logements disponibles.

    Args:
        request (HttpRequest): La requête HTTP.

    Returns:
        HttpResponse: La page HTML contenant les logements.
    """
    lettings_list = Letting.objects.all()
    logger.info("Chargement de la page index des lettings avec %d logements.", len(lettings_list))
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Vue de détail d’un logement.

    Affiche les infos d’un logement à partir de son identifiant.

    Args:
        request (HttpRequest): La requête HTTP.
        letting_id (int): ID du logement.

    Returns:
        HttpResponse: La page HTML contenant le logement.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    logger.info("Accès au détail du letting id %d : %s", letting.id, letting.title)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

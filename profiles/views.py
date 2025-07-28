from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def index(request):
    """
    Vue de la page d'accueil des profils.

    Récupère tous les profils et les affiche dans le template 'profiles/index.html'.

    Args:
        request (HttpRequest): La requête HTTP.

    Returns:
        HttpResponse: La page HTML contenant la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Vue de détail d'un profil utilisateur.

    Affiche les informations du profil correspondant au nom d'utilisateur donné.

    Args:
        request (HttpRequest): La requête HTTP.
        username (str): Le nom d'utilisateur.

    Returns:
        HttpResponse: La page HTML avec les infos du profil.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

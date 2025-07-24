from django.shortcuts import render
from profiles.models import Profile


# Récupère tous les profils utilisateurs pour la page d’accueil des profils
def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/profiles_index.html', context)


# Affiche les informations d’un utilisateur à partir de son nom d’utilisateur
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

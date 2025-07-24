from django.shortcuts import render
from lettings.models import Letting


# Récupère tous les logements disponibles pour la page des lettings
def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/lettings_index.html', context)


# Affiche les détails d’un logement en fonction de son ID
def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

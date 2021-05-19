from django.shortcuts import render
from tours.data import title, subtitle, description, departures, tours

def main_view(request):
    return render(request, 'tours/index.html', context={'title': title, 'subtitle': subtitle, 'description': description})

def departure_view(request, departure_id):
    departure = departures[departure_id]
    return render(request, 'tours/departure.html', context={'departure': departure})

def tour_view(request, tour_id):
    tour = tours[tour_id]
    return render(request, 'tours/tour.html', context={'tour': tour})

def custom_handler404(request, exception=None, template_name='tours/errors/404.html'):
    return render(request, template_name)

def custom_handler500(request, template_name='tours/errors/505.html'):
    return render(request, template_name)

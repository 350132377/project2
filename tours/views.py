from django.shortcuts import render
from tours.data import departures, tours
import random

def main_view(request):
    val = []
    for key, vl in tours.items():
        val.append(vl)
    return render(request, 'tours/index.html', context={'tours': random.sample(val, 6)})

def departure_view(request, departure_id):
    departure = departures[departure_id]
    val = []
    for key, vl in tours.items():
        val.append(vl)
    return render(request, 'tours/departure.html', context={'departure': departure, 'tours': random.sample(val, 6)})

def tour_view(request, tour_id):
    tour = tours[tour_id]
    return render(request, 'tours/tour.html', context={'tour': tour})

def custom_handler404(request, exception=None, template_name='tours/errors/404.html'):
    return render(request, template_name)

def custom_handler500(request, template_name='tours/errors/505.html'):
    return render(request, template_name)

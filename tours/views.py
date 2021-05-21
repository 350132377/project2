from django.shortcuts import render

from tours.data import departures, tours

from random import sample

def main_view(request):
    return render(request, 'tours/index.html', context={'tours': dict(sample(tours.items(), 6))})

def departure_view(request, departure_id):
    departure = departures[departure_id]
    departure1, result, keys = departure_id, [], []
    for k, tour in tours.items():
        if tour['departure'] == departure1:
            keys.append(k)
            result.append(tour)
    zipped = zip(keys, result)
    return render(request, 'tours/departure.html', context={'tours': zipped, 'departure': departure})

def tour_view(request, tour_id):
    tour = tours[tour_id]
    return render(request, 'tours/tour.html', context={'tour': tour})

def custom_handler404(request, exception=None, template_name='tours/errors/404.html'):
    return render(request, template_name)

def custom_handler500(request, template_name='tours/errors/505.html'):
    return render(request, template_name)

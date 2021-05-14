from django.shortcuts import render

tours = {
    1: 'Snowy Maple Resort ★★★★',
    2: 'Snowy Maple Resort ★★★★',
    3: 'Snowy Maple Resort ★★★★',
    4: 'Snowy Maple Resort ★★★★',
    5: 'Snowy Maple Resort ★★★★',
    6: 'Snowy Maple Resort ★★★★',
}

departures = {
    'dep1': 'Летим из Москвы',
    'dep2': 'Летим из Петербурга',
    'dep3': 'Летим из Новосибирска',
    'dep4': 'Летим из Екатеринбурга',
    'dep5': 'Летим из Казани',
}
def main_view(request):
    return render(request, 'tours/index.html')

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

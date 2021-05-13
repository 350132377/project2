from django.shortcuts import render

def main_view(request):
    return render(request, 'templates/tours/index.html')

def departure_view(request):
    return render(request, 'templates/tours/departure.html')

def tour_view(request):
    return render(request, 'templates/tours/tour.html')

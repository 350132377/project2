from tours.data import title, subtitle, description, departures, tours

def travel(request):
    return {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'departures': departures,
        'tours': tours,
    }
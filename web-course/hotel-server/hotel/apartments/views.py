from django.shortcuts import render

context = {
    'apartments' : [
  {
        'id': 1,
        'name': 'GRIFFIN SUITE',
        'description': '1 Bedroom Suite, 1 King, Sofa bed',
        'image': 'http://127.0.0.1:9000/hotel/images/image_1.png',
    },
    {
        'id': 2,
        'name': 'STUDIO SUITE',
        'description': '1 King, Sofa bed',
        'image': 'http://127.0.0.1:9000/hotel/images/image_3.png',
    },
    {
        'id': 3,
        'name': 'JUNIOR SUITE',
        'description': '1 King, Sofa bed',
        'image': 'http://127.0.0.1:9000/hotel/images/image_2.png',
    },
       {
        'id': 4,
        'name': 'Parking',
        'description': 'Лучшая парковка в гараже',
        'image': 'http://127.0.0.1:9000/hotel/images/parking.png',
    },
    {
        'id': 5,
        'name': 'Breakfast in room',
        'description': 'Восхитительный завтрак по утрам',
        'image': 'http://127.0.0.1:9000/hotel/images/image_4.png',
    },
    {
        'id': 6,
        'name': 'Disneyland trip',
        'description': 'Парк-развлечений для всей семьи',
        'image': 'http://127.0.0.1:9000/hotel/images/image.png',
    },
]
}

def index(request):
  return render(request, "apartments/hotel_menu.html", context)

def description(request):
  return render(request, "apartments/hotel_description.html")

def applicants(request):
  return render(request, "apartments/hotel_application.html")


def apartments(request):
    data = apartments    
    
    search = request.GET.get('name', "")
    if search:
        data = [apartment for apartment in apartments if search.lower() in apartment['name'].lower()]
    
    return render(request, '/apartments_menu.html', {"data": data})
from django.shortcuts import render

def index(request):
  return render(request, "services/index.html")

def description(request):
  return render(request, "services/index2.html")

def applicants(request):
  return render(request, "services/index3.html")

drivers = [
  {
        'id': 1,
        'name': 'GRIFFIN SUITE',
        'description': '1 Bedroom Suite, 1 King, Sofa bed',
        'image': 'http://127.0.0.1:8000/images/image_1.png',
    },
    {
        'id': 2,
        'name': 'STUDIO SUITE',
        'description': '1 King, Sofa bed',
        'image': 'http://127.0.0.1:8000/images/image_3.png',
    },
    {
        'id': 3,
        'name': 'JUNIOR SUITE',
        'description': '1 King, Sofa bed',
        'image': 'http://127.0.0.1:8000/images/image_2.png',
    },
       {
        'id': 4,
        'name': 'GRIFFIN SUITE',
        'description': '1 Bedroom Suite, 1 King, Sofa bed',
        'image': 'http://127.0.0.1:8000/images/image_1.png',
    },
    {
        'id': 5,
        'name': 'Breakfast in room',
        'description': 'Восхитительный завтрак по утрам',
        'image': 'http://127.0.0.1:8000/images/image_4.png',
    },
    {
        'id': 6,
        'name': 'Disneyland trip',
        'description': 'Парк-развлечений для всей семьи',
        'image': 'http://127.0.0.1:8000/images/image.png',
    },
]
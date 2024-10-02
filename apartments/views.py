from django.shortcuts import render
from datetime import date

applications = [
    {
        "id": 1,
        "from": "12.12.2024",
        "duration": '7 дней/ночей',
        "hotel_services": [2, 5, 6],
    },
    {
        "id": 2,
        "from": "15.12.2024",
        "duration": '10 дней/ночей',
        "hotel_services": [2, 4, 5, 6],
    },
    {
        "id": 3,
        "from": "17.12.2024",
        "duration": '12 дней/ночей',
        "hotel_services": [3, 6],
    }

]

def ordered(application_id):
    application = next((ap for ap in applications if ap['id']==application_id), None)
    cards_id = application['hotel_services']
    order_apartments = [card for card in card_apartments if card['id'] in cards_id]
    return order_apartments

def order(request, application_id):
    application = next((ap for ap in applications if ap['id']==application_id), None)
    order_apartments = ordered(application_id)
    return render(request, 'apartments/hotel_application.html', {'application':application, "order_apartments": order_apartments})

card_apartments = [
  {
        'id': 1,
        'name': 'GRIFFIN SUITE',
        'description': '1 Bedroom Suite, 1 King, Sofa bed',
        'image': 'http://127.0.0.1:9000/hotel/images/image_1.png',
        'price': '17,388₽',
        'details': "Полулюкс, 1 большая двуспальная кровать, Диван-кровать, Мини-холодильник, 59 кв.м., Гостиная/зона отдыха, Беспроводной доступ в Интернет (платно), Проводной доступ в Интернет (платно), Кофеварка/чайник",
    },
    {
        'id': 2,
        'name': 'STUDIO SUITE',
        'description': '1 King, Sofa bed',
        'image': 'http://127.0.0.1:9000/hotel/images/image_3.png',
        'price': '21,999₽',
        'details': 'Люкс-студио, 1 кровать размера "king-size", диван-кровать, мини-холодильник, 756 кв. футов/68 кв.м., гостиная/гостиная, обеденная зона, беспроводной интернет, за плату, проводной интернет, за плату, кофеварка/чайник',
    },
    {
        'id': 3,
        'name': 'JUNIOR SUITE',
        'description': '1 King, Sofa bed',
        'image': 'http://127.0.0.1:9000/hotel/images/image_2.png',
        'price': '25,768₽',
        'details': 'Представительский большой номер для гостей, 1 кровать размера "king-size", мини-холодильник, 525 кв. футов/47 кв.м., беспроводной интернет, за плату, проводной интернет, за плату, кофеварка/чайник',
    },
       {
        'id': 4,
        'name': 'Parking in hotel',
        'description': 'Лучшая парковка в гараже',
        'image': 'http://127.0.0.1:9000/hotel/images/parking.png',
        'price': '3,999₽/сутки',
        'details': "Паркинг расположен на закрытой территории гостиницы и оснащен видеонаблюдением, рассчитан на 150 мест, включая места не только для легковых автомобилей, а также для крупногабаритного транспорта, например,  туристических автобусов.",
    },
    {
        'id': 5,
        'name': 'Breakfast in room',
        'description': 'Восхитительный завтрак по утрам',
        'image': 'http://127.0.0.1:9000/hotel/images/image_4.png',
        'price': '1,999₽',
        'details': "Континентальный завтрак предполагает порционное питание, в которое обычно входят жареные яйца, бекон либо отварные сосиски, тосты, круассаны, овощи, чай или кофе – на выбор. В этом формате ассортимент уже.",
    },
    {
        'id': 6,
        'name': 'Disneyland trip',
        'description': 'Парк-развлечений для всей семьи',
        'image': 'http://127.0.0.1:9000/hotel/images/image.png',
        'price': '12,250₽',
        'details': "Диснейленд в Париже – это сказочное место, где посетители всех возрастов ненадолго возвращаются в детство и вновь переживают приятные эмоции от встречи с любимыми героями диснеевских мультфильмов. Отправляйтесь в месте с нами в поездку!",
    },
]

def index(request):
  data = card_apartments    

  application = next((ap for ap in applications if ap['id']==1), None)
  count = 0
  search = request.GET.get('search', '')
  if search:
      data = [apartment for apartment in card_apartments if search.lower() in apartment['name'].lower()]
  if application:
    count = len(application['hotel_services'])
    
  return render(request, 'apartments/hotel_menu.html', {"apartments": data, "search": search, 'application':application, 'count': count})



def apartments_detail(request, id_apartments):

    aps = next((ap for ap in card_apartments if ap['id'] == id_apartments ), None)
    if not aps:
        return get_object_or_404(aps)
    return render(request, 'apartments/hotel_description.html', {'apartments': aps})
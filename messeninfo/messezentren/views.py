import random

from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def Hotels(request, id):
    print('id')
    print(id)
    cursor = connection.cursor()
    cursor.execute(f'''SELECT firma, plz, strasse, text_en, lat, lon FROM `messezentren` WHERE zentren_id={id}''')
    columns = [col[0] for col in cursor.description]
    items = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    response = {
        'items': items,
        'main': {
            'firma': 'Not Found',
            'plz': 'Not Found',
            'strasse': 'Not Found'
        }
    }
    try:
        response['main'] = items[0]
    except Exception as e:
        print(e)

    return render(request, 'Hotels.html', response)


def get_flug_id(request):
    extra = request.GET.get('extra', None)
    response = {
        'id': 0
    }
    if extra:
        response['id'] = random.randrange(100)

    return JsonResponse(response)


def get_verkehr_id(request):
    extra = request.GET.get('extra', None)
    response = {
        'id': 0
    }
    if extra:
        response['id'] = random.randrange(100)

    return JsonResponse(response)

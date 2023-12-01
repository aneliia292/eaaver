from django.shortcuts import render


data = {
    'group': '3327, Python-3',
    'study': 'Alabuga Politech',
    'work': 'программистом',
    'name': 'Аюпова Анелия',
    'age': 16,
    'height': 164,
    'weight': 58,
    'phone': 89874920177,
    'Email': 'aneliia292@yandex.ru',
    'Telegram': '@wwssiidd'
}

def index(request):
    return render(request, 'work/index.html', context=data)

def about(request):
    return render(request, 'work/about.html', context=data)

def contacts(request):
    return render(request, 'work/contacts.html', context=data)

def form(request):
    return render(request, 'work/form.html', context=data)

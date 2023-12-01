from django.shortcuts import render


clients = [
    {'id': 1, 'name': 'Tom', 'lang': 'Python'},
    {'id': 2, 'name': 'Vasya', 'lang': 'C'},
    {'id': 3, 'name': 'Maks', 'lang': 'C++'},
    {'id': 4, 'name': 'Sanya', 'lang': 'Java'},
    {'id': 5, 'name': 'Merlin', 'lang': 'C#'},
]

def index(request):
    header = 'Данные пользователя'
    langs = ['python', 'c', 'C++', 'C#', 'JavasCript', 'java']
    user = {'name': 'Aneliya','age': 16}
    address = ('Neftekamsk', 13, 123)
    text = '<p style="background: #000; color: #fff; font-size: 40px">My text</p>'

    data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text}
    return render(request, 'index.html', context=data)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def client(request, id):
    return render(request, 'client.html', context={'id': id})


def clientsView(request):
    return render(request, 'clients.html', context={'clients': clients})
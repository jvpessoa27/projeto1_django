from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def sobre(request):
    return render(request, 'me_apague/temp.html')


def contato(request):
    return HttpResponse('contato')

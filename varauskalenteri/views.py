from django.http import HttpResponse
from django.shortcuts import render

from.models import Tapahtuma

def etusivu(request):
    tapahtumat = Tapahtuma.objects.all()
    context = {
        'tapahtumat': tapahtumat,
        }
    return render(request, 'etusivu.html', context)
    #return HttpResponse(vastaus)

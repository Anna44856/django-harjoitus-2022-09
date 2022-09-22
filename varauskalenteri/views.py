from django.http import HttpResponse
from django.shortcuts import render


def etusivu(request):
    return HttpResponse("Moi")

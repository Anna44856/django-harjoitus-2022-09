from django.http import HttpResponse
from django.shortcuts import render

from.models import Tapahtuma


def tapahtumalistaus(request):
    tapahtumat = Tapahtuma.objects.all()
    context = {
        'tapahtumat': tapahtumat,
        }
    return render(request, 'listaus.html', context)


def varaa_tapahtuma(request, id):
    tapahtuma = Tapahtuma.objects.get(id=id)
    context = {'tapahtuma': tapahtuma}

    if request.method == "POST":
        toiminto = request.POST.get("toiminto", "varaa")
        if toiminto == "varaa":
            varattu = tapahtuma.varaa(request.user)
            context["varattu"] = varattu
        elif toiminto == "peru":
            tapahtuma.poista_varaus(request.user)
            context["varattu"] = False
        else:
            raise ValueError(f"Tuntematon toiminto: {toiminto}")
    else: #GET
        varattu = tapahtuma.onko_varattu(request.user)
        context["varattu"] = varattu

    return render(request, 'varaa.html', context)

    
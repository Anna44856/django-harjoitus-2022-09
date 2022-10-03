from django.shortcuts import render


def etusivu(request):
    context = {
        "user": request.user,
    }
    return render(request, "etusivu.html", context)
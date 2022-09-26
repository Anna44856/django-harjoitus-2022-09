from django.urls import path

from .views import tapahtumalistaus, varaa_tapahtuma

urlpatterns = [
    path('', tapahtumalistaus, name="etusivu"),
    path('<int:id>/', varaa_tapahtuma),
]
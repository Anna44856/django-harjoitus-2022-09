from django.urls import path

from .views import tapahtumalistaus, varaa_tapahtuma

urlpatterns = [
    path('', tapahtumalistaus, name="tapahtumalistaus"),
    path('tapahtuma/<int:id>/', varaa_tapahtuma, name="varaus"),
]
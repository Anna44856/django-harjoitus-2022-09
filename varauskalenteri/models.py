import datetime

from django.db import models
from django.conf import settings



class Tapahtuma(models.Model):
    otsikko = models.CharField(max_length=200)
    kuvaus = models.TextField()
    alku = models.DateTimeField()
    loppu = models.DateTimeField()
    osallistujat = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        required=False,
        #blank=True,
        )
    paikkoja = models.IntegerField()

    def __str__(self):
        return f"{self.otsikko} ({self.alku}--{self.loppu})"

    def kesto(self) -> datetime.timedelta:
        return self.loppu - self.alku

    def kesto_tuntia(self):
        kesto = self.kesto()
        return kesto.total_seconds() / 3600

    def varaa(self, user):
        if user in self.osallistujat.all():
            return True
        osallistujia = self.osallistujat.all().count()
        if osallistujia + 1 > self.paikkoja:
            return False
        self.osallistujat.add(user)
        return True

    def onko_varattu(self, user):
        return (user in self.osallistujat.all())

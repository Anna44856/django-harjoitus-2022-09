from django.db import models


class Tapahtuma(models.Model):
    otsikko = models.CharField(max_length=200)
    kuvaus = models.TextField()
    alku = models.DateTimeField()
    loppu = models.DateTimeField()

    def __str__(self):
        return f"{self.otsikko} ({self.alku}--{self.loppu})"

    def kesto(self):
        return self.loppu - self.alku
        

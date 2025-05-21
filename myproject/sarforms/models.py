from django.db import models

class Form133(models.Model):
    incident_nr = models.IntegerField(null=True, blank=True)
    incident_naam = models.CharField(max_length=30)
    datum = models.DateField()
    locatie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.datum} - {self.incident_naam}"

class Form133Next(models.Model):
    incident_nr = models.IntegerField(null=True, blank=True)
    incident_naam = models.CharField(max_length=30, null=True, blank=True)
    locatie = models.CharField(max_length=100, null=True, blank=True)
    datum = models.DateField(null=True, blank=True)
    tijd = models.TimeField()
    team = models.CharField(max_length=50)
    bericht = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.incident_nr} - {self.tijd} - {self.team} - {self.bericht}"

from django.db import models

class Incident(models.Model):
    titel = models.CharField(max_length=100)
    datum = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titel
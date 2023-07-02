from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=30)
    tugilgan_yil = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30)

    def __str__(self):
        return self.ism

class Albom(models.Model):
    nom = models.CharField(max_length=70)
    sana = models.DateField(null=True,blank=True)
    rasm = models.FileField(null=True,blank=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Qoshiq(models.Model):
    nom = models.CharField(max_length=100)
    janr = models.CharField(max_length=50)
    davomiylik = models.DurationField(null=True,blank=True)
    fayl = models.FileField(null=True,blank=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ombor(models.Model):
    ism = models.CharField(max_length=30)
    dokon_nomi = models.CharField(max_length=30)
    maxsulot_turi = models.CharField(max_length=20, blank=True)
    manzil = models.CharField(max_length=25)
    tel_raqam = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.ism},{self.dokon_nomi}'

class Product(models.Model):
    nomi = models.CharField(max_length=30)
    brend_nomi = models.CharField(max_length=30, blank=True, default='-')
    kelgan_narx = models.IntegerField()
    sotuvdagi_narx = models.IntegerField()
    miqdor = models.SmallIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nomi},{self.brend_nomi}'

class Client(models.Model):
    ism = models.CharField(max_length=30)
    dokon_nomi = models.CharField(max_length=30)
    manzil = models.CharField(max_length=25)
    tel_raqam = models.CharField(max_length=15)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.ism},{self.dokon_nomi}'
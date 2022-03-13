from django.db import models
from django.contrib.auth.models import User
from main_app.models import *
# Create your models here.

class Stats(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    sanasi = models.DateTimeField(auto_now_add=True)
    miqdor = models.PositiveSmallIntegerField()
    umumiy_summa = models.IntegerField()
    tolandi = models.IntegerField()
    nasiya = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.client.ism} , {self.product.nomi}, ({self.miqdor}), {self.sanasi}"
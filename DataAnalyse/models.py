from django.db import models


class CollectData(models.Model):
    id = models.IntegerField(primary_key=True)
    cloths = models.IntegerField()
    underwear = models.IntegerField()
    sportswear = models.IntegerField()
    accessories = models.IntegerField()

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    nbr_children = models.IntegerField()
    career = models.CharField(max_length=100)
    shopping_price = models.IntegerField()
    collect_data = models.OneToOneField(CollectData, on_delete=models.CASCADE, null=True)
    
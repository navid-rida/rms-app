from django.db import models
from django.utils import timezone
# Create your models here.
class Rawmaterial(models.Model):
    name = models.CharField("Name of The Raw Material/ Ingredient", max_length=20)
    KG= 'KG'
    LITRE = 'LT'
    UNIT = 'UT'
    UNIT_CHOICES = (
        (KG,'Kilogram'),
        (LITRE, 'LITRE'),
        (UNIT, 'Unit'),
        )
    measurmentunit = models.CharField("Unit of measurement",max_length=8, choices=UNIT_CHOICES)
    VEGITABLES= 'VGT'
    MEAT = 'MT'
    GROCERIES = 'GRC'
    TYPE_CHOICES = (
        (VEGITABLES,'Vegitables'),
        (MEAT, 'Meat'),
        (GROCERIES, 'Groceries'),
        )
    type = models.CharField("Type of raw material",max_length=8, choices=TYPE_CHOICES)
    #address = models.TextField("Address of the branch")

    def __str__(self):
        return self.name

class Purchase(models.Model):
    rawmaterial = models.ForeignKey(Rawmaterial,on_delete=models.PROTECT, verbose_name='Name of Item to purchase')
    date = models.DateField("Date of purchase", default=timezone.now)
    quantity = models.IntegerField("Quantity of purchase", default=timezone.now)
    def __str__(self):
        return self.rawmaterial.name+" "+self.quantity+self.rawmaterial.measurmentunit+" "+"Purchased on:"+" "+self.date

class Item(models.Model):
    name = models.CharField("Name of The item", max_length=20)
    cost = models.FloatField("Cost of The item")

class Combos(models.Model):
    name = models.CharField("Name of The item", max_length=20)
    code = models.CharField("Code of the item", max_length=20)
    ONEPERSON= '1'
    TWOPERSON = '2'
    THREEPERSON = '3'
    COMBO_CHOICES = (
        (ONEPERSON,'1:1'),
        (TWOPERSON, '2:1'),
        (THREEPERSON, '3:1'),
        )
    type = models.CharField("Type of raw material",max_length=8, choices=COMBO_CHOICES)

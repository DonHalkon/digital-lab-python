from django.db import models

units = {'mg', 'kg', 'ml', 'l'}


# Create your models here.
class Compound(models.Model):
    shortName = models.CharField(max_length=200)
    iupacName = models.CharField(max_length=200)
    molecularFormula = models.CharField(max_length=200)
    structure = models.CharField(max_length=200)
    cid = models.CharField(max_length=200)


class ReagentLocation(models.Model):
    descr = models.CharField(max_length=200)


class Reagent(models.Model):
    receiptDate = models.DateField()
    storageLife = models.CharField(max_length=200)
    compoundId = models.IntegerField()
    amount = models.CharField(max_length=200)
    measurementUnits = models.SET(units)
    reagentLocation = models.IntegerField()
    comments = models.CharField(max_length=200)

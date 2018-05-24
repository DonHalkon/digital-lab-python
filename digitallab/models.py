from django.db import models

units = {'mg', 'kg', 'ml', 'l'}


# Create your models here.
class Compound(models.Model):
    shortName = models.CharField(max_length=200, unique=True, null=False)
    iupacName = models.CharField(max_length=1200, unique=True)
    molecularFormula = models.CharField(max_length=1200, unique=True)
    structure = models.CharField(max_length=10000, unique=True, null=False)
    cid = models.CharField(max_length=200, unique=True)


class ReagentLocation(models.Model):
    descr = models.CharField(max_length=1200, unique=True, null=False)


class Reagent(models.Model):
    receiptDate = models.DateField()
    storageLife = models.CharField(max_length=200)
    compoundId = models.ForeignKey(Compound, on_delete=models.CASCADE)
    amount = models.CharField(max_length=20)
    measurementUnits = models.SET(units)
    reagentLocation = models.ForeignKey(ReagentLocation, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200)

from django.db import models

units = (
    (1, ('mg')),
    (2, ('kg')),
    (3, ('g')),
    (4, ('ml')),
    (5, ('l')),
    (6, ('nl'))
)


# Create your models here.
class Compound(models.Model):
    shortName = models.CharField(max_length=200, unique=True, null=False)
    iupacName = models.CharField(max_length=1200, null=True)
    molecularFormula = models.CharField(max_length=1200, null=True)
    structure = models.CharField(max_length=10000, unique=True, null=False)
    cid = models.CharField(max_length=200, null=True)


class ReagentLocation(models.Model):
    descr = models.CharField(max_length=1200, unique=True, null=False)


class Reagent(models.Model):
    receiptDate = models.DateField()
    storageLife = models.CharField(max_length=200)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE, null=False)
    amount = models.CharField(max_length=20)
    measurementUnits = models.IntegerField(units)
    reagentLocation = models.ForeignKey(ReagentLocation, on_delete=models.CASCADE, null=False)
    comments = models.CharField(max_length=200)

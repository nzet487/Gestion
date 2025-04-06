from django.db import models

# Create your models here.

class Produit(models.Model):
    nomProduit = models.CharField(max_length=200)
    prixUnitaire = models.DecimalField(max_digits=10, decimal_places=2)
    dateCreation = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.nomProduit

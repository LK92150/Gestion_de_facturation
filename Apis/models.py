from django.db import models

# Create your models here.
class ApiModel(models.Model):
    num_fact = models.CharField(primary_key=True, max_length=25)
    coordonnees_client = models.CharField(max_length=150)
    coordonnees_entreprise = models.CharField(max_length=150)
    date_facture = models.DateField()
    nom_produit = models.CharField(max_length=50)
    quantite = models.IntegerField()
    prix_ht = models.FloatField()
    tva = models.FloatField()
    prix_ttc = models.FloatField()

    def __str__(self):
        return self.num_fact
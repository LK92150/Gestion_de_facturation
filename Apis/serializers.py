from rest_framework import serializers
from .models import ApiModel

class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiModel
        fields = ['num_fact','coordonnees_client','coordonnees_entreprise','date_facture','nom_produit','quantite','prix_ht','tva',
                  'prix_ttc'] 
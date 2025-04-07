from django import forms
from .models import Produit,Personne

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nomProduit','prixUnitaire']
class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom','prenom','telephone']
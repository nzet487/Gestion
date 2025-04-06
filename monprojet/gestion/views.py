from django.shortcuts import render,redirect,get_object_or_404
from .models import Produit
from .forms import ProduitForm

# Create your views here.


def liste_produits(request):
    produits = Produit.objects.all()
    return render(request,'gestion/liste.html',{'produits':produits})

def creer_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('liste_produits')
        
    else:
        form = ProduitForm()
    return render(request,'gestion/creer_produit.html',{'form':form})

def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)  # Récupérer le produit par ID
    produit.delete()  # Supprimer le produit de la base de données
    return redirect('liste_produits') 

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)  # Récupérer le produit par ID
    
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)  # Passer le produit existant au formulaire
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect('liste_produits')  # Rediriger vers la liste des produits
    else:
        form = ProduitForm(instance=produit)  # Pré-remplir le formulaire avec les données du produit

    return render(request, 'gestion/modifier_produit.html', {'form': form, 'produit': produit})
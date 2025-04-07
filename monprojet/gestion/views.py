from django.shortcuts import render,redirect,get_object_or_404
from .models import Produit,Personne
from .forms import ProduitForm,PersonneForm

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

def afficher_personne(request):
    personnes = Personne.objects.all()
    return render(request,'gestion/listepersonne.html',{'personnes':personnes})

def creer_personne(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('afficher_personne')
        
    else:
        form = PersonneForm()
    return render(request,'gestion/creer_personne.html',{'form':form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # ⚠️ Ici, tu peux ajouter ta logique d'authentification
        if username == "admin" and password == "admin":  # Ex. test simple
            return redirect('home')  # Rediriger vers la page d'accueil
        
        # Si échec : afficher la même page avec un message d’erreur
        return render(request, 'LoginPage.html', {'error': 'Identifiants incorrects'})
    
    return render(request, 'gestion/LoginPage.html')

def home(request):
    return render(request, 'gestion/home.html')
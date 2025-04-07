from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
    path('listeproduit', views.liste_produits, name='liste_produits'),
    path('creer',views.creer_produit,name='creer_produit'),
    path('supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),  # Nouvelle route
    path('modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'), 
    path('afficher',views.afficher_personne,name="afficher_personne"), # Nouvelle route
    path('creer_personne',views.creer_personne,name='creer_produit'),
    path('home/', views.home, name='home'),

]
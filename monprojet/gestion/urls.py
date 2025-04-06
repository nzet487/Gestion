from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('creer',views.creer_produit,name='creer_produit'),
    path('supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),  # Nouvelle route
    path('modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),  # Nouvelle route

]
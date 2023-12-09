from django.urls import path 

from .views import cadastrar_usuario, login, usuarios, logout_view


urlpatterns = [
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('', login, name='login'),
    path('usuarios/',usuarios, name='usuarios'),
    path('logout/',logout_view, name='logout'),
]
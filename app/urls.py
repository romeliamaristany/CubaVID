from django.urls import path
from .views import home, historia, tarjeta, listaHC, modificarHC, eliminarHC, registroUsuario, listaTV, modificarTV, eliminarTV, profile

urlpatterns = [
    path('', home, name="home"),
    path('historia/', historia, name="historia"),
    path('tarjeta/', tarjeta, name="tarjeta"),
    path('listaHC/', listaHC, name="listaHC"),
    path('modificarHC/<id>/', modificarHC, name="modificarHC"),
    path('eliminarHC/<id>/', eliminarHC, name="eliminarHC"),
    path('registroUsuario/', registroUsuario, name="registroUsuario"),
    path('listaTV/', listaTV, name="listaTV"),
    path('modificarTV/<id>/', modificarTV, name="modificarTV"),
    path('eliminarTV/<id>/', eliminarTV, name="eliminarTV"),
    path('profile/', profile, name="profile"),

    





]
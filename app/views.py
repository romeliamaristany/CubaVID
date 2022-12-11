from crypt import methods
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import is_valid_path
from .models import HC, TV
from .forms import HistoriaClinicaForm, CustomUserCreationForm, TarjetaVacunacionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json

# from django.core.paginator import Paginator
# from django.http import Http404

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


@permission_required('app.add_hc')
def historia(request):
    data = {
        'form': HistoriaClinicaForm()
    }
    if request.method == 'POST':
        formulario = HistoriaClinicaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Historia Clinica registrada")
        else:
            data["form"] = formulario
    return render(request, 'app/CrearHistoriaClinica.html', data)

#@login_required
@permission_required('app.view_hc')
def listaHC(request):
    historias = HC.objects.all()
   # page = request.GET.get('page',1)

  #  try:
   #     paginator = Paginator(historias, 8 )
    #    historias = paginator.page(page)
    #except: 
     #   raise Http404


    data = {
        'historias': historias
    }
    return render(request, 'app/listarHistoriaClinica.html', data)

@permission_required('app.change_hc')
def modificarHC(request, id):
    historias = get_object_or_404(HC, id=id)
    data = {
        'form': HistoriaClinicaForm(instance=historias)
    }
    if request.method == 'POST':
        formulario = HistoriaClinicaForm(data=request.POST, instance=historias, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Historia Clinica modificada")
            return redirect(to="listaHC")
            data["form"] = formulario
        else:
            data["form"] = formulario
    return render(request, 'app/modificarHistoriaClinica.html', data)

@permission_required('app.delete_hc')
def eliminarHC(request, id):
    historias = get_object_or_404(HC, id=id)
    historias.delete()
    messages.success(request, "Historia Clinica eliminada")
    return redirect(to="listaHC")


def registroUsuario(request):
    data = {
        'form': CustomUserCreationForm() 
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


def tarjeta(request):
    data = {
        'form': TarjetaVacunacionForm()
    }

    if request.method == 'POST':
      formulario = TarjetaVacunacionForm(data=request.POST)
      if formulario.is_valid():
          formulario.save()
          messages.success(request, "Tarjeta de Vacunación registrada")
      else:
          data["form"] = formulario

    return render(request, 'app/CrearTarjetaVacunacion.html', data)


#@login_required
@permission_required('app.view_tv')
def listaTV(request):
    targetas = TV.objects.all()

    data = {
        'targetas': targetas
    }
    return render(request, 'app/listarTarjetaVacunacion.html', data)


@permission_required('app.change_tv')
def modificarTV(request, id):
    tarjetas = get_object_or_404(TV, id=id)
    data = {
        'form': TarjetaVacunacionForm(instance=tarjetas)
    }
    if request.method == 'POST':
        formulario = TarjetaVacunacionForm(data=request.POST, instance=tarjetas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tarjeta de Vacunación modificada")
            return redirect(to="listaTV")
        else:
            data["form"] = formulario
    return render(request, 'app/modificarTarjetaVacunacion.html', data)


@permission_required('app.delete_tv')
def eliminarTV(request, id):
    tarjetas = get_object_or_404(TV, id=id)
    tarjetas.delete()
    messages.success(request, "Tarjeta de Vacunación eliminada")
    return redirect(to="listaTV")

def profile(request):
     
    return render(request, 'app/account.html')


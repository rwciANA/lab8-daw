from django.shortcuts import render, redirect, get_object_or_404
from .models import DestinosTuristicos
from .forms import DestinoForm

def index(request):
    dests = DestinosTuristicos.objects.all()
    return render(request, 'index.html', {'dests': dests})

def agregar(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DestinoForm()
    return render(request, 'agregar.html', {'form': form})

def modificar(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'modificar.html', {'form': form})

def eliminar(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('index')
    return render(request, 'eliminar.html', {'destino': destino})

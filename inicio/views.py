from django.shortcuts import render, redirect
from inicio.models import Remera
from inicio.forms import CreacionRemeraFormulario, BuscarRemera

#vista de inicio
def mi_vista(request):
    return render(request, 'index.html')

#vista para crear el objeto remera mediante uso de formularoi
def crear_remera(request):
    if request.method == "POST":
        formulario = CreacionRemeraFormulario(request.POST)
        
        #utilizo las validaciones de Django
        if formulario.is_valid():
            datos_correctos= formulario.cleaned_data
            
            remera = Remera(modelo=datos_correctos['modelo'], talle=datos_correctos['talle'], disenio=datos_correctos['disenio'], origen=datos_correctos['origen'])
            remera.save()
            
            return redirect(r'inicio:listar_remeras')
    
    formulario = CreacionRemeraFormulario()
    return render(request, r'crear_remera.html', {'formulario': formulario})

#vista del listado de remeras creadas
def lista_remeras(request):
    nombre_a_buscar = request.GET.get('disenio', None)
    
    if nombre_a_buscar:
        remeras = Remera.objects.filter(disenio__icontains=nombre_a_buscar)
    else:
        remeras = Remera.objects.all()
    formulario_busqueda = BuscarRemera()
    return render(request, r'lista_remeras.html', {'remeras': remeras,'formulario': formulario_busqueda})

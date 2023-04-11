from django.shortcuts import render, redirect

def mi_vista(request):
    return render(request, 'index.html')

def crear_remera(request):
    ...
from django.shortcuts import render
from .models import Asignacion
from django.http import HttpResponse

def healthCheck(request):
    return HttpResponse('ok')

def principal(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        nacionalidad = request.POST.get("nacionalidad")
        numero = request.POST.get("numero")

        if nombre and edad and nacionalidad:
            asignacion = Asignacion(nombre=nombre, edad=edad, nacionalidad=nacionalidad, numero=numero)
            asignacion.save()  
    asignaciones = Asignacion.objects.all()

    return render(request, "asignacion.html", {'asignaciones': asignaciones})





def siguiente(request):

    return render(request,"formulario.html",{})



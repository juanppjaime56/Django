from django.shortcuts import render
from .models import Asignacion

def principal(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        nacionalidad = request.POST.get("nacionalidad")

        if nombre and edad and nacionalidad:
            asignacion = Asignacion(nombre=nombre, edad=edad, nacionalidad=nacionalidad)
            asignacion.save()  
    asignaciones = Asignacion.objects.all()

    return render(request, "asignacion.html", {'asignaciones': asignaciones})





def siguiente(request):

    return render(request,"formulario.html",{})



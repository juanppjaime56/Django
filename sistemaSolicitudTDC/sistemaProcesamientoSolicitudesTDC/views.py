from django.shortcuts import render
from .models import Asignacion

def principal(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        nacionalidad = request.POST.get("nacionalidad")

        # Verificar si se proporcionan los datos
        if nombre and edad and nacionalidad:
            # Crear una nueva instancia de Asignacion con los datos recuperados
            asignacion = Asignacion(nombre=nombre, edad=edad, nacionalidad=nacionalidad)
            asignacion.save()  # Guardar la instancia en la base de datos

    # Obtener todas las asignaciones de la base de datos
    asignaciones = Asignacion.objects.all()

    return render(request, "asignacion.html", {'asignaciones': asignaciones})





def siguiente(request):

    return render(request,"formulario.html",{})



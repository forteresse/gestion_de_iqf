from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import Permission
#para el inicio de sesión
from django.contrib.auth import authenticate, login

# Create your views here.

    
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect('iqf_consultar_insumo')  # Redirige a la página de inicio después de iniciar sesión
            #return redirect('datos_generales',ruta='iqf_consultar_insumo.html')
            return datos_generales(request,ruta='iqf_consultar_insumo.html')
        else:
            error_message = "Credenciales inválidas ingrese sus datos de nuevo"  # Puedes mostrar un mensaje de error en la plantilla
            return render(request, 'iniciar_sesion.html', {'error_message': error_message})
    else:
        return render(request, 'iniciar_sesion.html')

#ruta contiene la plantilla objetivo
def datos_generales(request, ruta):
    contexto={
        'nombre_usuario' : request.user.first_name,
        'apellidos' : request.user.last_name,
    }
    return render(request,ruta, contexto)
    
def recuperar_contrasena(request):
    return render(request, 'recuperar_contrasena.html')
    

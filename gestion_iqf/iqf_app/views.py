#from django.http import HttpResponse
from django.shortcuts import render, redirect
#importamos todas nuestras tablas para usarlas en las distintas vistas
from .models import *
from django.contrib.auth.models import Permission
#para el inicio de sesión
from django.contrib.auth import authenticate, login
#mostrar error 404 en casos determinados
from django.shortcuts import get_object_or_404
#para actualizar insumo
from datetime import datetime
#para reciclar informacion entre plantillas y no acceder base de datosfrom django.http import QueryDict
from django.http import QueryDict
#para emitir mensajes de error,de exito o mas
from django.contrib import messages
# para proteger las vistas se requerira el inicio de sesion para que se muestren
from django.contrib.auth.decorators import login_required
#realizamos test de pase de usuario
from django.contrib.auth.decorators import user_passes_test


# funciones para proteger vistas de usuarios admitidos
def es_almacen_iqf(user):
    return user.groups.filter(name='almacen_iqf').exists()
    
def es_laboratorista_iqf(user):
    return user.groups.filter(name='laboratorista_iqf').exists()
# Create your views here.


""" ejemplo usando httpresponse
def home(request):
    return HttpResponse("<h1>HOla munod</h1>")
"""

def home(request):
    permisos = Permission.objects.all()
    return render(request, "inicio.html", {"users_permisos": permisos})

#FUNCIONES DE INICIO DE SESIÓN

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            #inicio de sesion segun al grupo al que corresponda
            if es_almacen_iqf(user):
                return redirect('iqf_consultar_insumo')
            elif es_laboratorista_iqf(user):
                return redirect('lab_solicitar_insumo')

            #return redirect('iqf_consultar_insumo')  # Redirige a la página de inicio después de iniciar sesión
            
            #return redirect('datos_generales',ruta='iqf_consultar_insumo.html')
            #return datos_generales(request,ruta='iqf_consultar_insumo.html')
        else:
            error_message = "Credenciales inválidas ingrese sus datos de nuevo"  # Puedes mostrar un mensaje de error en la plantilla
            return render(request, 'iniciar_sesion.html', {'error_message': error_message})
    else:
        return render(request, 'iniciar_sesion.html')

def recuperar_contrasena(request):
    return render(request, 'recuperar_contrasena.html')
    
"""
#ruta contiene la plantilla objetivo
def datos_generales(request, ruta):
    contexto={
        'nombre_usuario' : request.user.first_name,
        'apellidos' : request.user.last_name,
    }
    return render(request,ruta, contexto)
"""
#FUNCIONES MÓDULO CONSULTAR INSUMO
@login_required
@user_passes_test(es_almacen_iqf, login_url='/acceso_denegado/')
def iqf_consultar_insumo(request):
    nombre = request.user.first_name
    apellidos = request.user.last_name
    
    #mostramos la primera tabla que da a conocer los insumos que se encuentran en el almacen
    #select from iq_fiscalizados_inventarios where inventarios_id='almaceniqf'
    insumos_almacen = iq_fiscalizados_inventarios.objects.filter(inventarios_id='almaceniqf')
    insumos_datos = []
    datos_extraidos = [] # referente al inventario en donde se encuentran dichos insumos
    insumos_fiscalizados= iq_fiscalizados.objects.all()

    for i in insumos_fiscalizados:
        print("nombre",i.nombre)
        print("nombre",i.formula)
        
    insumos_fiscalizados2= iq_fiscalizados.objects.filter(id='7664-93-9')
    for i in insumos_fiscalizados2:
        print("nombre 2 ",i.nombre)
        print("nombre 2 ",i.formula)
        
    """
    print("ta buscando")
    for i in insumos_almacen:
        print (i.iq_fiscalizados_id)
        insumos_datos.append(iq_fiscalizados.objects.filter(id=i.iq_fiscalizados_id))
        print ("aquiiii")"""
    
    for insumo in insumos_almacen:
        id_comp=insumo.iq_fiscalizados_id
        print("tipo ",id_comp.id)
        
        iq_fiscalizado = iq_fiscalizados.objects.filter(id=id_comp.id)
        
        print("esto deberia ser ", iq_fiscalizado)
        insumos_datos.append(iq_fiscalizado)
    
    for i in range(len(insumos_datos)):
        for j in insumos_datos[i]:
            datos_extraidos.append(j)
     
    iqf_imagen_base = 'iqf/iqf_default.jpg'
    return render (request, "iqf_consultar_insumo.html", {'nombre_usuario':nombre, 
    'apellidos':apellidos, 'insumos_almacen':insumos_almacen, 'datos_extraidos':datos_extraidos, 'iqf_imagen':iqf_imagen_base})

@login_required
def iqf_llenar_campos(request, insumo_id):
    return redirect("iqf_consultar_insumo")
"""
def iqf_barra_busqueda(request):
    if 'busqueda' in request.GET:
        busqueda = request.GET['busqueda']
        insumos = Insumo.objects.filter(nombre__icontains=busqueda)
    else:
        insumos = Insumo.objects.all()
    return render(request, 'buscar_insumos.html', {'insumos': insumos})
"""

@login_required
@user_passes_test(es_almacen_iqf, login_url='/acceso_denegado/')
def iqf_barra_busqueda(request):
    busqueda_realizada = True
    
    nombre = request.user.first_name
    apellidos = request.user.last_name
    
    #mostramos la primera tabla que da a conocer los insumos que se encuentran en el almacen
    insumos_almacen = iq_fiscalizados_inventarios.objects.filter(inventarios_id='almaceniqf')
    insumos_datos = []
    datos_extraidos = []
    insumos_fiscalizados= iq_fiscalizados.objects.all()
    
    for insumo in insumos_almacen:
        id_comp=insumo.iq_fiscalizados_id
        print("tipo ",id_comp.id)
        iq_fiscalizado = iq_fiscalizados.objects.filter(id=id_comp.id)
        print("esto deberia ser ", iq_fiscalizado)
        insumos_datos.append(iq_fiscalizado)
    
    for i in range(len(insumos_datos)):
        for j in insumos_datos[i]:
            datos_extraidos.append(j)
    
    if 'busqueda' in request.GET:
        nombre_busqueda = request.GET['busqueda']
        producto_encontrado = iq_fiscalizados.objects.filter(nombre__icontains=nombre_busqueda).first()
        # Marcar el insumo encontrado
    else:
        producto_encontrado = None
    
    iqf_imagen_base = 'iqf/iqf_default.jpg'
    
    contexto = {'nombre_usuario':nombre, 
                'apellidos':apellidos, 
                'insumos_almacen':insumos_almacen, 
                'datos_extraidos':datos_extraidos,'producto_encontrado': producto_encontrado, 
                'iqf_imagen': iqf_imagen_base,
                'busqueda_realizada': busqueda_realizada}
    return render(request, 'iqf_consultar_insumo.html', contexto)

@login_required
@user_passes_test(es_almacen_iqf, login_url='/acceso_denegado/')
def iqf_mostrar_detalle(request, producto_encontrado_id):
    iqf = get_object_or_404(iq_fiscalizados, id=producto_encontrado_id)
    # Aquí puedes agregar lógica adicional si es necesario
    return render(request, 'iqf_consultar_insumo.html', {'iqf_encontrado': iqf})
    
# los desencadenantes de esta funcion envian id del producto

@login_required
@user_passes_test(es_almacen_iqf, login_url='/acceso_denegado/')
def iqf_mostrar_detalle2(request, producto_encontrado_id):

    iqf = get_object_or_404(iq_fiscalizados, id=producto_encontrado_id)
    
    nombre = request.user.first_name
    apellidos = request.user.last_name
    
    #mostramos la primera tabla que da a conocer los insumos que se encuentran en el almacen
    insumos_almacen = iq_fiscalizados_inventarios.objects.filter(inventarios_id='almaceniqf')
    insumos_datos = []
    datos_extraidos = []
    insumos_fiscalizados= iq_fiscalizados.objects.all()
    
    for insumo in insumos_almacen:
        id_comp=insumo.iq_fiscalizados_id
        print("tipo ",id_comp.id)
        iq_fiscalizado = iq_fiscalizados.objects.filter(id=id_comp.id)
        print("esto deberia ser ", iq_fiscalizado)
        insumos_datos.append(iq_fiscalizado)
    
    for i in range(len(insumos_datos)):
        for j in insumos_datos[i]:
            datos_extraidos.append(j)
            
    # obtener investigacion relacionada
    print("\ncomprobaciooon\n")
    iqf_investigacion = iqf.lineas_investigacion_id.nombre
    print(" la investigacion es : ",iqf.lineas_investigacion_id.nombre)
    
    #obtener objetivo relacionado
    #necesitamos identificar cual objetivo pertnece a dicho insumo manytomany
    objetivos = []
    print("el id del insumos que ingreso: ", iqf.id)
    for i in iq_fiscalizados_objetivos.objects.all():
        print("no se: ", i.objetivos_id.objetivo)
        
    for i in iq_fiscalizados_objetivos.objects.all():
        print("hhhh: ", i.iq_fiscalizados_id)
        
    iqf_objetivo = iq_fiscalizados_objetivos.objects.filter(iq_fiscalizados_id=iqf.id)
    #al almacenar iqf_objetivo este es un array pero como solo tenemos un insumo ingresando
    #entonces solo debemos obtener el [0]
    """
    print("el objetivo es: ", iqf_objetivo[0].objetivos_id.objetivo)
    iqf_objetivo = iqf_objetivo[0].objetivos_id.objetivo
    """
    for i in range(len(iqf_objetivo)):
        objetivos.append(iqf_objetivo[i].objetivos_id.objetivo)
    
    #obtener imagen relacionada
    iqf_imagen = iqf.imagen_iqf
    print ("la imagen es : ", iqf_imagen)
    
    #obtener fechas antigua y reciente contiene la hora asi que aplicamos date para obtener solo fecha
    iqf_fecha_a = iqf.fecha_v_antigua.date()
    iqf_fecha_r = iqf.fecha_v_reciente.date()
    print("las fechas son antigua ", iqf_fecha_a, "reciente ", iqf_fecha_r)
    
    #obtener cantidad total del insumo
    cant_total = iq_fiscalizados_inventarios.objects.filter(iq_fiscalizados_id=iqf.id)
    print ("total de insumo : ", cant_total[0].cantidad)
    cant_total = cant_total[0].cantidad
    
    #obtener id del insumo para editar datos en "ACTUALIZAR"
    id_iq_fiscalizado = iqf.id
    print("el id es -> ", id_iq_fiscalizado)
    
    #este es momentaneo para mostrar ficha directamente
    print("\n ID del insumo cuya FICHA se mostrará: ", id_iq_fiscalizado, "\n")
    ficha_iqf = iq_fiscalizados.objects.filter(id=id_iq_fiscalizado)
    print (ficha_iqf)
    ficha_requerida=ficha_iqf[0].fichas_tecnicas_id.nombre_pdf
    print ("\n esta es la ficha : ", ficha_requerida, "\n")
    
    
    contexto = {'nombre_usuario':nombre, 
                'apellidos':apellidos, 
                'insumos_almacen':insumos_almacen, 
                'datos_extraidos':datos_extraidos,
                'iqf_investigacion':iqf_investigacion,
                'objetivos': objetivos,
                'iqf_imagen': iqf_imagen,
                'fecha_antigua': iqf_fecha_a,
                'fecha_reciente': iqf_fecha_r,
                'cantidad_total':cant_total,
                'iqf_id': id_iq_fiscalizado,
                'producto_encontrado':iqf,
                'iqf_ficha':ficha_requerida}
    return render (request, "iqf_consultar_insumo.html", contexto)
    
"""
    productoslistados = productos.objects.all()
    datos = productos.objects.values('nombre','imagen')
    laboratorio= 'Sanidad Vegetal'
    
    if request.method == 'POST':
        item_name = request.POST['productox']
        # Get the image file for the item
        imagen_correspondiente = 'img/' + item_name + '.jpg'
        context = {"productos":productoslistados, "imagen_correspondiente":imagen_correspondiente, "laboratorio":laboratorio}
        print("\n\n toy funcionando", imagen_correspondiente)
        return render(request, 'gestionar.html', context)
"""

@login_required
@user_passes_test(es_almacen_iqf, login_url='/acceso_denegado/')
def iqf_actualizar(request, producto_encontrado_id):
    #print("usuario actual -> ", request.user.id)
    usuario_actual=request.user.id
    inventario_objetivo = inventarios.objects.filter(auth_user_id_id=usuario_actual)
    print ("--- inventario_objetivo : ", inventario_objetivo)
    #print("datos extraidos -> ", datos_extraidos)
    inventario_id=[]
    
    for i in range(len(inventario_objetivo)):
        inventario_id.append(inventario_objetivo[i].id)
        
    print ("\n id de inventario: ", inventario_id[0], "\n")
    print ("\n id del insumo : ", producto_encontrado_id, "\n")
    inventario_id = inventario_id[0]
    
    if request.method == 'POST':
        #recuperamos los datos ocultos que se devolvieron de la anterior plantilla
        
        #para cambiar la fecha
      
        #para cambiar la cantidad
        cant = request.POST['cantidad']
        fech = request.POST['fecha']
        
        #identificamos los insumos correspondientes al almacen
        actualizar_cantidad = iq_fiscalizados_inventarios.objects.filter(inventarios_id=inventario_id, iq_fiscalizados_id=producto_encontrado_id)
        actualizar_cantidad = actualizar_cantidad[0]
        print("\n array de insumos",actualizar_cantidad.cantidad,"\n")
        
        actualizar_cantidad.cantidad += int(cant)
        actualizar_cantidad.save()
        
        #enviamos el mensaje de exito
        messages.success(request, 'El producto se actualizó correctamente.')
        
        return redirect('iqf_mostrar_detalle2', producto_encontrado_id)
        """
        for i in range(len(actualizar_cantidad)):
            #print ("\n este es el id : ", actualizar_cantidad[i].id)
            print ("\n este es el id de fiscalizados : ", actualizar_cantidad[i].id)
            print ("\n este es el id a comparar : ", producto_encontrado_id)
            if actualizar_cantidad[i].iq_fiscalizados_id == producto_encontrado_id:
                print(" actualizando correctamente")
        """  
        #identificamos el insumo que queremos actualizar dentro de los insumos del almacen
        
        
        # Obtener la fecha y hora actual del sistema
        #fecha_hora_actual = datetime.now()
        fecha_hora_actual = fech
        
        # Obtener la hora y los minutos actuales
        #hora_actual = fecha_hora_actual.hour
        #minutos_actuales = fecha_hora_actual.minute
        
        # Ahora puedes asignar estos valores a tu campo iqf_inventarios.fecha
        #iqf_inventarios.fecha = fecha_hora_actual.replace(hour=hora_actual, minute=minutos_actuales, second=0, microsecond=0)
        
        #Actualizar cantidad de insumo en el almacen
        #iqf_inventario.cantidad += cant
        #iqf.fecha_v_reciente = fech
    else:
        messages.error(request, 'Se canceló la actualizacion.')
        return redirect('iqf_mostrar_detalle2', producto_encontrado_id)


#VER FICHA TECNICA
@login_required
@user_passes_test(es_almacen_iqf, login_url='/acceso_denegado/')
def iqf_ver_ficha(request, iqf_id):

    nombre = request.user.first_name
    apellidos = request.user.last_name
    
    print("\n ID del insumo cuya FICHA se mostrará: ", iqf_id, "\n")
    ficha_iqf = iq_fiscalizados.objects.filter(id=iqf_id)
    print (ficha_iqf)
    ficha_requerida=ficha_iqf[0].fichas_tecnicas_id.nombre_pdf
    print ("\n esta es la ficha : ", ficha_requerida, "\n")
    
    contexto = {'nombre_usuario':nombre, 
                'apellidos':apellidos,
                'iqf_ficha':ficha_requerida}
    
    return render(request, 'ver_ficha.html',contexto)
    
    
    
    
#VISTAS PARA LOS LABORATORISTAS
@login_required
@user_passes_test(es_laboratorista_iqf, login_url='/acceso_denegado/')
def lab_solicitar_insumo(request):
    nombre = request.user.first_name
    apellidos = request.user.last_name
    
    contexto = {'nombre_usuario':nombre, 
                'apellidos':apellidos}
    
    return render(request, "laboratorista/solicitar_insumo.html", contexto)

#FUNCIONES GENERALES CON BASE DE DATOS
#def obtener_insumos(request, insumo):
    
#FUNCIONES PRUEBA

#lo siguiente es muestra

@login_required
def inicio(request):
    nombre = request.user.first_name
    apellidos = request.user.last_name
    permisos = Permission.objects.all()
    
    return render(request, "inicio.html",{'nombre_usuario':nombre, 'apellidos':apellidos, 'users_permisos': permisos})
    

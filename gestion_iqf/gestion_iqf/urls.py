"""
URL configuration for gestion_iqf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iqf_app.views import * #funciones, vistas de la aplicacion iqf_app
from django.conf import settings
from django.conf.urls.static import static

# si la plantilla es statica no necesita el parámetro "name" caso contrario usar name para obtener datos
# el name puede ser obligatorio para navegar entre distintas rutas y el nombre de la ruta se siga correctamente
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', iniciar_sesion),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('inicio/', inicio, name='inicio'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('recuperar_contrasena/', recuperar_contrasena, name='recuperar_contrasena'),
    #path('datos_generales/<str:ruta>/', datos_generales, name='datos_generales'),
    path('iqf_consultar_insumo/',iqf_consultar_insumo, name='iqf_consultar_insumo'),
    path('iqf_barra_busqueda/',iqf_barra_busqueda, name='iqf_barra_busqueda'),
    #mostrar detalles de insumo
    path('iqf_mostrar_detalle/<str:producto_encontrado_id>/',iqf_mostrar_detalle, name='iqf_mostrar_detalle'),
    path('iqf_mostrar_detalle2/<str:producto_encontrado_id>/',iqf_mostrar_detalle2, name='iqf_mostrar_detalle2'),
    path('iqf_llenar_campos/<str:insumo_id>/',iqf_llenar_campos, name='iqf_llenar_campos'),
    #path('iqf_actualizar/<str:producto_encontrado_id>/',iqf_actualizar, name='iqf_actualizar'),
    path('iqf_actualizar/',iqf_actualizar, name='iqf_actualizar'),
    path('iqf_ver_ficha/<str:iqf_id>/', iqf_ver_ficha, name='iqf_ver_ficha'),
    path('iqf_habilitar/', iqf_habilitar, name='iqf_habilitar'),
    #path('iqf_revisar_solicitud/<str:nombre_archivo>/', iqf_revisar_solicitud, name='iqf_revisar_solicitud'),
    path('habilitar_solicitud/<str:id_solicitud>/', habilitar_solicitud, name='habilitar_solicitud'),
    path('rechazar_solicitud/<str:id_solicitud>/', rechazar_solicitud, name='rechazar_solicitud'),
    path('iqf_reporte_gasto/', iqf_reporte_gasto, name='iqf_reporte_gasto'),
    
    #rutas de laboratoristas
    path('lab_solicitar_insumo', lab_solicitar_insumo, name='lab_solicitar_insumo'),
    path('soli_actualizar', soli_actualizar, name='soli_actualizar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

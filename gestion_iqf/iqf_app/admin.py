"""
from django.contrib import admin
from .models import * # areas, facultades, escuelas, inventarios, fichas_tecnicas, medidas, lineas_investigacion, objetivos, iq_fiscalizados, denominaciones

@admin.register(areas)
class AreasAdmin(admin.ModelAdmin):
    pass

@admin.register(facultades)
class FacultadesAdmin(admin.ModelAdmin):
    pass

@admin.register(escuelas)
class EscuelasAdmin(admin.ModelAdmin):
    pass

@admin.register(inventarios)
class InventariosAdmin(admin.ModelAdmin):
    pass

@admin.register(fichas_tecnicas)
class FichasTecnicasAdmin(admin.ModelAdmin):
    pass

@admin.register(medidas)
class MedidasAdmin(admin.ModelAdmin):
    pass

@admin.register(lineas_investigacion)
class LineasInvestigacionAdmin(admin.ModelAdmin):
    pass

@admin.register(objetivos)
class ObjetivosAdmin(admin.ModelAdmin):
    pass

@admin.register(iq_fiscalizados)
class IqFiscalizadosAdmin(admin.ModelAdmin):
    pass

@admin.register(denominaciones)
class DenominacionesAdmin(admin.ModelAdmin):
    pass
"""
# Register your models here.

from django.contrib import admin
from .models import * #areas, facultades, escuelas, inventarios, fichas_tecnicas, medidas, lineas_investigacion, objetivos, iq_fiscalizados, denominaciones
from django.contrib.admin import TabularInline

@admin.register(titulos)
class titulos(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    
@admin.register(perfil_usuario)
class perfil_usuario_admin(admin.ModelAdmin):
    list_display = ['user', 'titulo']

@admin.register(areas)
class areas_admin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(facultades)
class facultades_admin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'areas_id']

@admin.register(escuelas)
class escuelas_admin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'facultades_id']

class iq_fiscalizados_inventarios_inline(admin.TabularInline):
    model=iq_fiscalizados_inventarios
    extra=1

@admin.register(inventarios)
class inventarios_admin(admin.ModelAdmin):
    inlines = [iq_fiscalizados_inventarios_inline,]
    list_display = ['id', 'nombre', 'condicion', 'escuelas_id', 'auth_user_id']

@admin.register(fichas_tecnicas)
class fichas_tecnicas_admin(admin.ModelAdmin):
    list_display = ['id', 'nombre_pdf']

@admin.register(medidas)
class medidas_admin(admin.ModelAdmin):
    list_display = ['id', 'unidad']

@admin.register(lineas_investigacion)
class lineas_investigacion_admin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(objetivos)
class objetivos_admin(admin.ModelAdmin):
    list_display = ['id', 'objetivo']

@admin.register(pecosas)
class pecosas_admin(admin.ModelAdmin):
    list_display = ['id', 'pecosa_pdf']

@admin.register(nombres_marca)
class nombres_marca_admin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(marcas)
class marcas_admin(admin.ModelAdmin):
    list_display = ['id', 'cod_articulo', 'concentracion', 'fecha_v']
    
@admin.register(iq_fiscalizados)
class iq_fiscalizados_admin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'formula', 'imagen_iqf', 'fichas_tecnicas_id', 'medidas_id']

@admin.register(iq_fiscalizados_lineas_investigacion)
class iq_fiscalizados_lineas_investigacion_admin(admin.ModelAdmin):
    list_display = ['iq_fiscalizados_id', 'lineas_investigacion_id']

@admin.register(iq_fiscalizados_objetivos)
class iq_fiscalizados_objetivos_admin(admin.ModelAdmin):
    list_display = ['iq_fiscalizados_id', 'objetivos_id']

@admin.register(iq_fiscalizados_pecosas)
class iq_fiscalizados_pecosas_admin(admin.ModelAdmin):
    list_display = ['cantidad', 'iq_fiscalizados_id', 'pecosas_id']

@admin.register(iq_fiscalizados_marcas)
class iq_fiscalizados_marcas_admin(admin.ModelAdmin):
    list_display = ['iq_fiscalizados_id', 'marcas_id']

"""
@admin.register(iq_fiscalizados_inventarios)
class iq_fiscalizados_inventarios_admin(admin.ModelAdmin):
    list_display = ['cantidad', 'iq_fiscalizados_id', 'inventarios_id']
"""


@admin.register(denominaciones)
class denominaciones_admin(admin.ModelAdmin):
    list_display = ['conjunto', 'iq_fiscalizados']
    
@admin.register(noti_estados)
class noti_estados_admin(admin.ModelAdmin):
    list_display = ['estado']
    
@admin.register(notificaciones_user)
class notificaciones_user_admin(admin.ModelAdmin):
    list_display = ['solicitud', 'fecha_envio', 'emisor_id', 'receptor_id', 'noti_estados_id']
    
@admin.register(iq_fiscalizados_notificaciones_user)
class iq_fiscalizados_notificaciones_user_admin(admin.ModelAdmin):
    list_display = ['iq_fiscalizados_id', 'notificaciones_user_id', 'cantidad']

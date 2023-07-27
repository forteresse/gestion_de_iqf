from django.db import models
from django.contrib.auth.models import User
#no se esta usando porque no pretendemos crear una tabla que hereda atributos de user principal
#from django.contrib.auth.models import AbstractUser
#usamos la siguiente libreria para añadir datos a alguna tabla en este caso usuario

# Create your models here.



#añadidos a usuario
class titulos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

#aumentamos el campo genero a la tabla de usuarios
class perfil_usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.ForeignKey(titulos, on_delete=models.SET_NULL, null=True, blank=True)

# parte de dependencias
class areas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, unique=True)

class facultades(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    nombre = models.CharField(max_length=100)
    areas_id = models.ForeignKey(areas, on_delete=models.CASCADE)

class escuelas(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    nombre = models.CharField(max_length=100)
    facultades_id = models.ForeignKey(facultades, on_delete=models.CASCADE)

class inventarios(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    nombre = models.CharField(max_length=100)
    condicion = models.BooleanField()
    escuelas_id = models.ForeignKey(escuelas, on_delete=models.CASCADE)
    auth_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

## parte 2

class fichas_tecnicas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_pdf = models.FileField(upload_to='fichas_t/') #models.FileField()

class medidas(models.Model):
    id = models.AutoField(primary_key=True)
    unidad = models.CharField(max_length=25)

class lineas_investigacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)

class objetivos(models.Model):
    id = models.AutoField(primary_key=True)
    objetivo = models.CharField(max_length=500)

class pecosas(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    pecosa_pdf = models.FileField(upload_to='pecosas/')

class nombres_marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, null=True, blank=True)

class marcas(models.Model):
    id = models.AutoField(primary_key=True)
    cod_articulo = models.CharField(max_length=60, null=True, blank=True)
    concentracion = models.FloatField(null=True, blank=True)
    fecha_v = models.DateTimeField(null=True, blank=True)
    nombre = models.CharField(max_length=60, null=True, blank=True)

class iq_fiscalizados(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=100)
    formula = models.CharField(max_length=50)
    #imagen_iqf = models.BinaryField()
    imagen_iqf = models.ImageField(null=True, blank=True, upload_to = 'iqf')
    fecha_v_antigua = models.DateTimeField()
    fecha_v_reciente = models.DateTimeField()
    fichas_tecnicas_id = models.ForeignKey(fichas_tecnicas, on_delete=models.CASCADE)
    medidas_id = models.ForeignKey(medidas, on_delete=models.CASCADE)
    lineas_investigacion = models.ManyToManyField(lineas_investigacion, through='iq_fiscalizados_lineas_investigacion', blank=True)
    inventarios = models.ManyToManyField(inventarios, through='iq_fiscalizados_inventarios')
    objetivos = models.ManyToManyField(objetivos, through='iq_fiscalizados_objetivos')
    pecosas = models.ManyToManyField(pecosas, through='iq_fiscalizados_pecosas')
    marcas = models.ManyToManyField(marcas, through='iq_fiscalizados_marcas')
    
    """
    #relaciones de muchos a muchos de tablas "objetivos" e "inventarios"
    inventarios = models.ManyToManyField('inventarios', through=iq_fiscalizados_inventarios)
    objetivos = models.ManyToManyField('objetivos')
    """
class iq_fiscalizados_lineas_investigacion(models.Model):
    iq_fiscalizados_id = models.ForeignKey('iq_fiscalizados', on_delete=models.CASCADE, db_column='iq_fiscalizados_id')
    lineas_investigacion_id = models.ForeignKey(lineas_investigacion, on_delete=models.CASCADE, db_column='lineas_investigacion_id')

class iq_fiscalizados_inventarios(models.Model):
    cantidad = models.IntegerField()
    iq_fiscalizados_id = models.ForeignKey('iq_fiscalizados', on_delete=models.CASCADE, db_column='iq_fiscalizados_id')
    inventarios_id = models.ForeignKey(inventarios, on_delete=models.CASCADE, db_column='inventarios_id')
    
class iq_fiscalizados_objetivos(models.Model):
    iq_fiscalizados_id = models.ForeignKey('iq_fiscalizados', on_delete=models.CASCADE, db_column='iq_fiscalizados_id')
    objetivos_id = models.ForeignKey(objetivos, on_delete=models.CASCADE, db_column='objetivos_id')

class iq_fiscalizados_pecosas(models.Model):
    cantidad= models.IntegerField(null=True, blank=True)
    iq_fiscalizados_id = models.ForeignKey('iq_fiscalizados', on_delete=models.CASCADE, db_column='iq_fiscalizados_id', blank=True)
    pecosas_id = models.ForeignKey(pecosas, on_delete=models.CASCADE, db_column='pecosas_id', blank=True)

class iq_fiscalizados_marcas(models.Model):
    iq_fiscalizados_id = models.ForeignKey('iq_fiscalizados', on_delete=models.CASCADE, db_column='iq_fiscalizados_id')
    marcas_id = models.ForeignKey(marcas, on_delete=models.CASCADE, db_column='marcas_id')

class denominaciones(models.Model):
    conjunto = models.CharField(max_length=400)
    iq_fiscalizados = models.ForeignKey(iq_fiscalizados, on_delete=models.CASCADE)
    
class noti_estados(models.Model):
    estado = models.CharField(max_length=50)
    
class notificaciones_user(models.Model):
    solicitud = models.FileField(upload_to='solicitudes/', null=True, blank=True)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    fecha_revision = models.DateTimeField(null=True, blank=True)
    emisor_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='emisor_id', related_name='emisor_id')
    receptor_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='receptor_id', related_name='receptor_id')
    noti_estados_id = models.ForeignKey(noti_estados, on_delete=models.CASCADE, db_column='noti_estados_id')
    iq_fiscalizado = models.ManyToManyField(iq_fiscalizados, through='iq_fiscalizados_notificaciones_user')
    #añadidos
    nro_oficio = models.IntegerField(null=True, blank=True)
    
class iq_fiscalizados_notificaciones_user(models.Model):
    iq_fiscalizados_id = models.ForeignKey(iq_fiscalizados, on_delete=models.CASCADE, db_column='iq_fiscalizados_id')
    notificaciones_user_id = models.ForeignKey(notificaciones_user, on_delete=models.CASCADE, db_column='notificaciones_user_id')
    cantidad = models.IntegerField(null=True, blank=True)



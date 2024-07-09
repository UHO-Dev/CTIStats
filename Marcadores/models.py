from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import (FACULTADES_CHOICES,
        TIPO, 
        CARACTER, 
        DEPARTAMENTOS_CHOICES, 
        PRESENCIALIDAD, 
        TIPO_PROYECTO_CHOICES, 
        SUBTIPO_PROYECTO_CHOICES,
        APROBACION, 
        FACULTADES_CHOICES, 
        SECTOR_ESTRATEGICO_CHOICES,   
        LINEA_INVESTIGACION_CHOICES, 
        ESTADO_PROYECTO_CHOICES, 
        APROBACION,
        CARACTER_EVENTO,
        PAIS
                   ) 

#########Usuarios#########
CATEGORIAS_CIENTIFICAS = (
    ('Investigador Agregado', 'Investigador Agregado'),
    ('Investigador Auxiliar', 'Investigador Auxiliar'),
    ('Investigador Titular', 'Investigador Titular'),
)

CATEGORIAS_DOCENTES = (
    ('Licenciado', 'Licenciado'),
    ('Maestria', 'Maestria'),
    ('Doctorado', 'Doctorado'),
)

ROLES_USUARIO = (
    ('administrador', 'administrador'),
    ('vicedecano', 'vicedecano'),
    ('vicerrector', 'vicerrector'),
    ('investigador', 'investigador'),
)

class Investigador(AbstractUser):
    rol = models.CharField(max_length=20, choices=ROLES_USUARIO, blank=False, null=False, verbose_name='Rol de Usuario', default='Investigador')
    categoria_cientifica = models.CharField(choices=CATEGORIAS_CIENTIFICAS, max_length=22, blank=False, null=False, verbose_name='Categoría Científica')
    categoria_docente = models.CharField(choices=CATEGORIAS_DOCENTES, max_length=20, blank=False, null=False, verbose_name='Categoría Docente')
    area = models.CharField(max_length=100, blank=False, null=False)
    perfil_google = models.URLField(blank=True, null=True)
    perfil_researchgate = models.URLField(blank=True, null=True)
    orci = models.CharField(max_length=10, unique=True)
    ci = models.CharField(max_length=11, unique=True)
    facultad = models.CharField(max_length=50, blank = False, null = False, choices = FACULTADES_CHOICES, default= 'Seleccione...')


    def __str__(self):
        return self.username
    


#Modelo de Autores
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    
#Modelo Proyectos
class Proyecto(models.Model):
    codigo_proyecto = models.CharField(max_length=100, unique=True)
    nombre_proyecto = models.CharField(max_length=255)
    jefe_proyecto = models.ManyToManyField(Investigador, verbose_name= 'Jefe de Proyecto')
    area_uho = models.CharField(max_length=100, choices=FACULTADES_CHOICES)
    departamento = models.CharField(max_length=100, choices=DEPARTAMENTOS_CHOICES)
    tipo_proyecto = models.CharField(max_length=4, choices=TIPO_PROYECTO_CHOICES)
    subtipo_proyecto = models.CharField(max_length=4, choices=SUBTIPO_PROYECTO_CHOICES, blank=True, null=True)
    entidades_participantes = models.TextField()
    sector_estrategico = models.CharField(max_length=100, choices=SECTOR_ESTRATEGICO_CHOICES)
    linea_investigacion = models.CharField(max_length=100, choices=LINEA_INVESTIGACION_CHOICES)
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField()
    estado_proyecto = models.CharField(max_length=10, choices=ESTADO_PROYECTO_CHOICES)
    cantidad_participantes = models.IntegerField()
    cantidad_participantes_uho = models.IntegerField()
    cantidad_estudiantes = models.IntegerField()
    cantidad_participantes_otras_entidades = models.IntegerField()
    cantidad_colaboradores = models.IntegerField()
    cantidad_colaboradores_uho = models.IntegerField()
    cantidad_estudiantes_gce = models.IntegerField()
    cantidad_colaboradores_otras_entidades = models.IntegerField()
    cantidad_estudiantes_segundo_ano = models.IntegerField()
    cantidad_cuadros_uho = models.IntegerField()
    presupuesto_planificado = models.DecimalField(max_digits=10, decimal_places=2)
    aprobacion = models.CharField(max_length=10, blank=False, null=False, choices=APROBACION, default= 'Pendiente')

    def __str__(self):
        return self.codigo_proyecto


		
#Modelo de Pogramas
class Programa(models.Model):
    codigo_programa = models.CharField(max_length=100, unique=True)
    nombre_programa = models.CharField(max_length=255)
    director_programa = models.ManyToManyField(Investigador, verbose_name= 'Director de Pograma')
    facultad = models.CharField(max_length=100, choices=FACULTADES_CHOICES)
    departamento = models.CharField(max_length=100, choices=DEPARTAMENTOS_CHOICES)
    tipo_programa = models.CharField(max_length=4, choices=TIPO_PROYECTO_CHOICES)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado_programa = models.CharField(max_length=10, choices=ESTADO_PROYECTO_CHOICES)
    presupuesto_asignado = models.DecimalField(max_digits=10, decimal_places=2)
    presupuesto_utilizado = models.DecimalField(max_digits=10, decimal_places=2)
    aprobacion = models.CharField(max_length=50, blank = False, null = False, choices = APROBACION, default= 'Pendiente')
    
    def __str__(self):
        return self.codigo_programa
    
#Modelo de Eventos

class Evento(models.Model):
    caracter = models.CharField(max_length=50, choices=CARACTER, default='Seleccione...')
    tipo = models.CharField(max_length=50, choices=TIPO, default='Seleccione...')
    presencialidad = models.CharField(max_length=50, choices=PRESENCIALIDAD, default='Seleccione...')
    titulo = models.CharField(max_length=200)
    autores =  models.ManyToManyField(Investigador, verbose_name= 'Autores')
    isbn = models.CharField(max_length=13)
    publicacion = models.URLField( null=True)
    fecha = models.DateField()
    facultad =  models.CharField(max_length=50, blank = False, null = False, choices = FACULTADES_CHOICES, default= 'Seleccione...')
    certificado = models.FileField(upload_to='eventos/')
    aprobacion = models.CharField(max_length=50, blank = False, null = False, choices = APROBACION, default= 'Pendiente')
    

    def __str__(self):
        return self.titulo
    
class PubliSeriada(models.Model):
    issn = models.CharField(max_length=9) 
    doi = models.CharField(max_length=9) 
    fecha_creacion = models.DateField()
    categoriaCientifica =  models.CharField(max_length=50, blank = False, null = False, choices = CATEGORIAS_CIENTIFICAS, default= 'Seleccione...')
    titulo = models.CharField(max_length=200)
    editorial =  models.CharField(max_length=200, default= 'Editorial...')
    facultad =  models.CharField(max_length=50, blank = False, null = False, choices = FACULTADES_CHOICES, default= 'Seleccione...')
    departamento =  models.CharField(max_length=50, blank = False, null = False, choices =  DEPARTAMENTOS_CHOICES, default= 'Seleccione...')
    autores = models.ManyToManyField(Investigador, verbose_name= 'Autores')
    pais =  models.CharField(max_length=50, blank = False, null = False, choices =  PAIS, default= 'Seleccione...')
    aprobacion = models.CharField(max_length=50, blank = False, null = False, choices = APROBACION, default= 'Pendiente')
    
    
    def __str__(self):
        return self.titulo

#Publicacion Unica, generalmente es un capitulo unico de un libro
class PubliUnica(models.Model):
    isbn = models.CharField(max_length=13)
    editorial =  models.CharField(max_length=200, default= 'Editorial...')
    capitulo = models.CharField(max_length=9, null=True)
    volumen = models.CharField(max_length=9, null=True)
    fecha_creacion = models.DateField()
    categoriaCientifica =  models.CharField(max_length=50, blank = False, null = False, choices = CATEGORIAS_CIENTIFICAS , default= 'Seleccione...')
    aprobacion = models.CharField(max_length=50, blank = False, null = False, choices = APROBACION, default= 'Pendiente')
    titulo = models.CharField(max_length=200)
    facultad =  models.CharField(max_length=50, blank = False, null = False, choices = FACULTADES_CHOICES, default= 'Seleccione...')
    departamento =  models.CharField(max_length=50, blank = False, null = False, choices =  DEPARTAMENTOS_CHOICES, default= 'Seleccione...')
    autores = models.ManyToManyField(Investigador, verbose_name= 'Autores')
    pais =  models.CharField(max_length=50, blank = False, null = False, choices =  PAIS, default= 'Seleccione...')
    aprobacion = models.CharField(max_length=50, blank = False, null = False, choices = APROBACION, default= 'Pendiente')

    def __str__(self):
        return self.titulo

    
#Premio

class Premio(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    aprobado =  models.CharField(max_length=50,null=True)
    facultad =  models.CharField(max_length=50, blank = False, null = False, choices = FACULTADES_CHOICES, default= 'Seleccione...')
    autores =  models.ManyToManyField(Investigador, verbose_name= 'Premiados')
    tipo = models.CharField(max_length=50, choices=TIPO, default='Seleccione...')
    caracter_premio = models.CharField(max_length=50, choices=CARACTER_EVENTO, default='Seleccione...')
    aprobacion = models.CharField(max_length=50, blank = False, null = False, choices = APROBACION, default= 'Pendiente')
    url = models.URLField((""), max_length=200)

    def __str__(self):
        return self.titulo

 
 
 
 
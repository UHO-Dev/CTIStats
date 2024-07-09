
#Caracter del evento

CARACTER = [
        ('','Seleccione...'),
        ('Congreso','Congreso'),
        ('Jornada','Jornada'),
        ('Foro','Foro'),
        ('Conferencia','Conferencia'),
        ('Panel','Panel'),
        ('Simposio','Simposio'),
        ('Mesab Redonda','Mesa Redonda'),
        ('Taller','Taller'),
        ('Seminario','Seminario'),
        ('Convencion','Converncion'),
        ('Encuentro','Encuentro'),
]

DEPARTAMENTOS_CHOICES = [
        ('CECID', 'CECID'),
        ('CEGEDEL', 'CEGEDEL'),
        ('CENFOLAB', 'CENFOLAB'),
        ('AFITCOMB', 'AFITCOMB'),
        ('CEGO', 'CEGO'),
        ('CECE', 'CECE'),
        ('CEAR', 'CEAR'),
        ('CADCAN', 'CADCAN'),
        # Add other departments and centers as needed
    ]
ESTADO_PROYECTO_CHOICES = [
        ('Normal', 'Normal'),
        ('Atrasado', 'Atrasado'),
        ('Terminado', 'Terminado'),
        ('Cancelado', 'Cancelado'),
        ('Prórroga', 'Prórroga'),
    ]


TIPO_PROYECTO_CHOICES = [
        ('PAPN', 'Proyectos Asociados a Programas Nacionales'),
        ('PAPS', 'Proyectos Asociados a Programas Sectoriales'),
        ('PAPT', 'Proyectos Asociados a Programas Territoriales'),
        ('PNAP', 'Proyectos No Asociados a Programas'),
    ]

SUBTIPO_PROYECTO_CHOICES = [
        ('PI', 'Proyectos Institucionales'),
        ('PE', 'Proyectos Empresariales'),
        ('PNE', 'Proyectos con Entidades No Empresariales y de la Administración Pública'),
        ('PDL', 'Proyectos de Desarrollo Local'),
        ('PRCI', 'Proyectos en Relación con la Colaboración Internacional'),
    ]

SECTOR_ESTRATEGICO_CHOICES = [
        ('Sector productor de alimentos', 'Sector productor de alimentos'),
        ('Industria Ligera', 'Industria Ligera'),
        ('Servicios técnicos profesionales', 'Servicios técnicos profesionales'),
        ('Industria', 'Industria'),
        ('Agroindustria azucarera y sus derivados', 'Agroindustria azucarera y sus derivados'),
        ('Industria farmacéutica, biotecnológica y', 'Industria farmacéutica, biotecnológica y'),
        ('Turismo', 'Turismo'),
        ('Logística integrada de redes e instalaciones', 'Logística integrada de redes e instalaciones'),
        ('Logística integrada de transporte', 'Logística integrada de transporte'),
        ('Telecomunicaciones', 'Telecomunicaciones'),
        ('Electroenergético', 'Electroenergético'),
        ('Construcciones', 'Construcciones'),
        # Add other sectors as needed
    ]

LINEA_INVESTIGACION_CHOICES = [
        ('Línea 1', 'Línea de Investigación 1'),
        # Add other lines as needed
    ]
    
PRESENCIALIDAD = [
    ('','Seleccione...'),
	('Presencial','Presencial'),
	('Virtual','Virtual'),
	('Mixto','Mixto'),
]


FACULTADES_CHOICES = [
    ('','Seleccione...'),
    ('FACOL','FACOL'),
    ('FACFID','FACFID'),
    ('FACFID','FACFID'),
    ('FACCE','FACCE'),
    ('FACID','FACFID'),
    ('FACCEC','FACCEC'),
    ('FACSOC','FACSOC'),
    ('FACCINA','FACCINA'),
    ('FACING','FACCINA'),
    ('FACINM','FACINM'),
    ]


SECTOR_ESTRATEGICO_CHOICES = [
    ('Sector 1', 'Sector Estratégico 1'),
    ('Sector 2', 'Sector Estratégico 2'),
    
 ]

AREA = [
    ('','Seleccione...'),
    ('Enseñanza Militar','Enseñanza Militar'),
    ('CUM Urbano Noris','CUM Urbano Noris'),
    ('CUM Banes','CUM Banes'),
    ('CEGEDEL','CEGEDEL'),
    ('DCTI','DCTI'),
    ('DCTI','DCTI'),
    ('FACOL','FACOL'),
    ('FACFID','FACFID'),
    ('Tegnología Educativa','Tegnología Educativa'),
    ('FACFID','FACFID'),
    ('FACCE','FACCE'),
    ('FACID','FACFID'),
    ('FACCEC','FACCEC'),
    ('FACSOC','FACSOC'),
    ('FACCINA','FACCINA'),
    ('FACING','FACCINA'),
    ('FACINM','FACINM'),
]

Categoria = [
	('Funcionando','Funcionando'),
	('Roto','Roto'),
	('Baja','Baja'),
	('Definir','Definir'),
]

Departamento = [
    ('','Seleccione...'),
	('Dep1','Dep1'),
	('Dep2','Dep2'),
	('Dep3','Dep4'),
	('Dep4','Dep5'),
    ]

APROBACION = [
    ('Pendiente','Pendiente'),
    ('No Valido','No Valido'),
	('Aprobado','Aprobado'),
]

TIPO = [
	('Nacional','Nacional'),
	('Regional','Regional'),
	('Internacional','Internacional'),
    ]

CARACTER_EVENTO = [
    ('','Ninguno...'),
	('Forum Ciencia Tecnica}','Forum Ciencia Tecnica'),
	('Forum Nacionales Estudiantiles','Forum Nacionales Estudiantiles'),
    ('Jornadas Cientificas Estudiantiles','Jornadas Cientificas Estudiantiles'),
	
]

PAIS = [
	('Cuba','Cuba'),
	('Otro','Otro')
]
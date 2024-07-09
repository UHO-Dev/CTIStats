from django.contrib import admin
from .models import Evento, PubliSeriada, PubliUnica, Proyecto, Programa, Premio, Investigador
admin.site.register(Evento)
admin.site.register(PubliUnica)
admin.site.register(PubliSeriada)
admin.site.register(Proyecto)
admin.site.register(Programa)
admin.site.register(Premio)
admin.site.register(Investigador)


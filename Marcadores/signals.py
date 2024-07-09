from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PubliUnica, PubliSeriada, Evento, Programa, Proyecto, Premio

@receiver(post_save, sender=PubliUnica)
def publiunica_edit(sender, instance, updated = True, **kwargs):
	if updated:
		instance.aprobacion = "Pendiente"
		instance.save()

@receiver(post_save, sender=PubliSeriada)
def publiseriada_edit(sender, instance, updated = True, **kwargs):
	if updated:
		instance.aprobacion = "Pendiente"
		instance.save()

@receiver(post_save, sender=Evento)
def publiseriada_edit(sender, instance, updated = True, **kwargs):
	if updated:
		instance.aprobacion = "Pendiente"
		instance.save()

@receiver(post_save, sender=Programa)
def publiseriada_edit(sender, instance, updated = True, **kwargs):
	if updated:
		instance.aprobacion = "Pendiente"
		instance.save()
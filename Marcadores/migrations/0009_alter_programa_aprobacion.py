# Generated by Django 5.0.4 on 2024-06-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marcadores', '0008_alter_evento_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='aprobacion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], default='Pendiente', max_length=50),
        ),
    ]

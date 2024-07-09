# Generated by Django 5.0.4 on 2024-06-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marcadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='aprobacion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], default='Pendiente', max_length=50),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='rol',
            field=models.CharField(choices=[('administrador', 'administrador'), ('vicedecano', 'vicedecano'), ('vicerrector', 'vicerrector'), ('investigador', 'investigador')], default='Investigador', max_length=20, verbose_name='Rol de Usuario'),
        ),
        migrations.AlterField(
            model_name='premio',
            name='aprobacion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], default='Pendiente', max_length=50),
        ),
        migrations.AlterField(
            model_name='premio',
            name='aprobado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='programa',
            name='aprobacion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='aprobacion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='publiseriada',
            name='aprobacion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], default='Pendiente', max_length=50),
        ),
        migrations.AlterField(
            model_name='publiunica',
            name='aprobacion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Valido', 'No Valido'), ('Aprobado', 'Aprobado')], default='Pendiente', max_length=50),
        ),
    ]

# Generated by Django 5.0.4 on 2024-06-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marcadores', '0005_alter_programa_departamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premio',
            name='aprobado',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

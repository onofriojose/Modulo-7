# Generated by Django 4.2.3 on 2023-08-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relaciones', '0002_tipocombustible'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelocarro',
            name='tipo_combustible',
            field=models.ManyToManyField(to='relaciones.tipocombustible'),
        ),
    ]

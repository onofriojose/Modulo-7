# Generated by Django 4.2.2 on 2023-08-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_productos_f_vencimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='f_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]

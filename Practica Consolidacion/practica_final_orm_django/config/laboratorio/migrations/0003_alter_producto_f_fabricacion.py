# Generated by Django 4.2.4 on 2023-08-09 01:27

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_alter_directorgeneral_laboratorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2015, 1, 1))]),
        ),
    ]

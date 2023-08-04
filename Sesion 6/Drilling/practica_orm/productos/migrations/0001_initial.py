# Generated by Django 4.2.2 on 2023-07-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
    ]

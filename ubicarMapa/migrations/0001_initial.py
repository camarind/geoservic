# Generated by Django 3.0.5 on 2020-04-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]

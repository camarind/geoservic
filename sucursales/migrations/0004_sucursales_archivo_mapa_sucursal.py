# Generated by Django 3.0.3 on 2020-04-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0003_auto_20200427_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursales',
            name='archivo_mapa_sucursal',
            field=models.FileField(null=True, upload_to='mapaSucursales/%Y/%m/%d'),
        ),
    ]
# Generated by Django 2.0.8 on 2018-09-27 05:43

import WebAdminRadio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0002_auto_20180926_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmento',
            name='imagen',
            field=models.ImageField(upload_to=WebAdminRadio.models.segmento_file_location),
        ),
    ]

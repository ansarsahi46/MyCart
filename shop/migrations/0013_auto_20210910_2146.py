# Generated by Django 3.1.6 on 2021-09-10 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210910_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 10, 21, 45, 59, 815295)),
        ),
    ]
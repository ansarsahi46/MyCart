# Generated by Django 3.1.6 on 2021-03-30 04:26

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210329_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]

# Generated by Django 3.1.6 on 2021-10-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogPosts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=1000)),
                ('head0', models.CharField(max_length=1000)),
                ('chead0', models.CharField(max_length=10000)),
                ('head1', models.CharField(max_length=1000)),
                ('chead1', models.CharField(max_length=10000)),
                ('head2', models.CharField(max_length=1000)),
                ('chead2', models.CharField(max_length=10000)),
                ('publish_date', models.DateField()),
                ('post_image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
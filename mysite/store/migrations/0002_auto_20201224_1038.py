# Generated by Django 3.1.3 on 2020-12-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
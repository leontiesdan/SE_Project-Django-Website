# Generated by Django 3.1.3 on 2020-12-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_profile_cartalbums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cartAlbums',
            field=models.ManyToManyField(null=True, to='store.Album'),
        ),
    ]

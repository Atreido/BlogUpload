# Generated by Django 4.2.7 on 2023-11-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.URLField(default='http://placehold.it/900x300'),
        ),
    ]

# Generated by Django 2.2 on 2020-05-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='address'),
            preserve_default=False,
        ),
    ]

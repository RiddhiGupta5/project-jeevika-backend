# Generated by Django 2.2 on 2020-05-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_donation_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

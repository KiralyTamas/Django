# Generated by Django 4.0.3 on 2022-03-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.CharField(default='', max_length=40, verbose_name='Tanár'),
        ),
    ]

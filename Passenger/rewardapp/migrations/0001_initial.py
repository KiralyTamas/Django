# Generated by Django 4.0.3 on 2022-03-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40, verbose_name='Vezeték Név')),
                ('lastName', models.CharField(max_length=40, verbose_name='Kereszt Név')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Cam')),
                ('reward_point', models.IntegerField(verbose_name='Jutalom Pontok')),
            ],
        ),
    ]

# Generated by Django 2.1.1 on 2019-10-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default='', max_length=20, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='', max_length=20, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='', max_length=20, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(default='', max_length=10, verbose_name='phone'),
        ),
    ]
# Generated by Django 2.2.2 on 2019-10-23 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 23, 20, 38, 32, 190147), verbose_name='date commented'),
        ),
    ]

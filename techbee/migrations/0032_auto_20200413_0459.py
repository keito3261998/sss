# Generated by Django 3.0.1 on 2020-04-13 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0031_auto_20200413_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_meta',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]

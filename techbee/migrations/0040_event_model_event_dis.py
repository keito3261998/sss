# Generated by Django 3.0.1 on 2020-04-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0039_auto_20200417_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_model',
            name='event_dis',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]

# Generated by Django 3.0.1 on 2020-04-03 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0019_auto_20200331_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts_model',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='techbee.categories_model'),
        ),
    ]

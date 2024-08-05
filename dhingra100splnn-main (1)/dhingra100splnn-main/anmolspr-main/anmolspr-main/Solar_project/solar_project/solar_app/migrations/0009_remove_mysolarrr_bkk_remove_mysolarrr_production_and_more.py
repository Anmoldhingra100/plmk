# Generated by Django 5.0.6 on 2024-07-30 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0008_alter_mysolarrr_bkk_alter_mysolarrr_production_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysolarrr',
            name='bkk',
        ),
        migrations.RemoveField(
            model_name='mysolarrr',
            name='production',
        ),
        migrations.RemoveField(
            model_name='mysolarrr',
            name='total',
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Hourly_temperature_and_humidity',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Investor_power_distribution',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Monthly_sales',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Performance',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Solar_generation',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Today_production',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Total_panels',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Weather_prediction',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='Weekly_revenue',
            field=models.IntegerField(default=0, max_length=400),
        ),
    ]

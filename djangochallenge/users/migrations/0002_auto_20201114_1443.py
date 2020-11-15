# Generated by Django 3.1.2 on 2020-11-14 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='area_code',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Código de área'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='country_code',
            field=models.CharField(max_length=4, verbose_name='Código do país'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999)], verbose_name='Número'),
        ),
    ]
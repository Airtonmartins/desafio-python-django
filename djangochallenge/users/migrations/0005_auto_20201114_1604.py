# Generated by Django 3.1.2 on 2020-11-14 19:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201114_1602'),
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
        migrations.AlterField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Sobrenome'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-14 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201114_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='users.user', verbose_name='Usuário'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0005_rename_nombre_proyecto_contaduria_id_nombre_proyecto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contaduria',
            name='id_nombre_proyecto',
        ),
        migrations.AddField(
            model_name='contaduria',
            name='nombre_proyecto',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

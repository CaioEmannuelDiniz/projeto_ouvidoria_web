# Generated by Django 5.1.2 on 2024-10-15 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouvidoria_web', '0006_reclamacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacao',
            name='classificacao_insatisfacao',
            field=models.IntegerField(),
        ),
    ]

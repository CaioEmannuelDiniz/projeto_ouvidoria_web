# Generated by Django 5.1.2 on 2024-10-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouvidoria_web', '0009_denuncia_feedback_denuncia_status_elogio_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='feedback',
            field=models.TextField(default='', null=True),
        ),
    ]

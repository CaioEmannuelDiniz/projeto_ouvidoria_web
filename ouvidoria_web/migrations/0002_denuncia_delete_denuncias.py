# Generated by Django 5.1.2 on 2024-10-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouvidoria_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_completo', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.TextField(max_length=15)),
                ('tipo_denuncia', models.TextField(max_length=20)),
                ('arquivo', models.FileField(blank=True, upload_to='documentos/denuncia')),
                ('descricao', models.TextField()),
                ('preferencia_contato', models.TextField(max_length=20)),
                ('comentario', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Denuncias',
        ),
    ]

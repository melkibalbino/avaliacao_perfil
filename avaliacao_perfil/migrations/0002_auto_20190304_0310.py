# Generated by Django 2.1.7 on 2019-03-04 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao_perfil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comportamento',
            old_name='perfil_id',
            new_name='perfil',
        ),
        migrations.RenameField(
            model_name='motivacao',
            old_name='perfil_id',
            new_name='perfil',
        ),
        migrations.RenameField(
            model_name='pergunta',
            old_name='avaliacao_id',
            new_name='avaliacao',
        ),
        migrations.RenameField(
            model_name='pontodamelhoria',
            old_name='perfil_id',
            new_name='perfil',
        ),
        migrations.RenameField(
            model_name='pontoforte',
            old_name='perfil_id',
            new_name='perfil',
        ),
        migrations.RenameField(
            model_name='resposta',
            old_name='perfil_id',
            new_name='perfil',
        ),
        migrations.RenameField(
            model_name='resposta',
            old_name='pergunta_id',
            new_name='pergunta',
        ),
    ]

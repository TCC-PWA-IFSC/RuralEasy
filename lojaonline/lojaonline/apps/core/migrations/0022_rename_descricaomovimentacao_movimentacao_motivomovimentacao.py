# Generated by Django 4.2 on 2023-10-24 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_rename_idtouro_inseminacao_idvaca_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimentacao',
            old_name='descricaoMovimentacao',
            new_name='motivoMovimentacao',
        ),
    ]
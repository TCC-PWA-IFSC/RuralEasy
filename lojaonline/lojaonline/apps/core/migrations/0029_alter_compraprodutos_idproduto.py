# Generated by Django 4.2 on 2023-10-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_rename_nomeprodsanitario_prodsanitario_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compraprodutos',
            name='idProduto',
            field=models.CharField(default='Padrao', max_length=100),
        ),
    ]

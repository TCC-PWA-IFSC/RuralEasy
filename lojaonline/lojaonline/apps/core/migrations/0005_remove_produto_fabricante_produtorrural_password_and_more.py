# Generated by Django 4.2 on 2023-07-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_produtorrural_cpf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='fabricante',
        ),
        migrations.AddField(
            model_name='produtorrural',
            name='password',
            field=models.CharField(default='senha', max_length=100),
        ),
        migrations.AddField(
            model_name='produtorrural',
            name='telefone',
            field=models.CharField(default='telefone', max_length=100),
        ),
        migrations.AddField(
            model_name='produtorrural',
            name='user',
            field=models.CharField(default='user', max_length=100),
        ),
        migrations.DeleteModel(
            name='Fabricante',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]

# Generated by Django 4.2 on 2023-10-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_animal_animal_pai_animal_numerogestacoes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inseminacao',
            old_name='idTouro',
            new_name='idVaca',
        ),
        migrations.AddField(
            model_name='inseminacao',
            name='identificacaoTouro',
            field=models.CharField(default='Padrao', max_length=100),
        ),
    ]

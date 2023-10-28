# Generated by Django 4.2 on 2023-08-09 12:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_prodsanitario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalidadeAnimalVenda', models.CharField(default='Padrao', max_length=100)),
                ('valorAnimalVenda', models.FloatField(default='0.0')),
                ('dataVenda', models.DateField(default=datetime.date.today)),
                ('pesoAnimalVenda', models.FloatField(default='0.0')),
                ('precoAtualArrobaKg', models.FloatField(default='0.0')),
                ('observacaoVenda', models.CharField(default='Padrao', max_length=100)),
                ('idAnimalVenda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.animal')),
            ],
        ),
    ]
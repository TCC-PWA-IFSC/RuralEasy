# Generated by Django 4.2 on 2023-08-08 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_veterinario_alter_animal_brinco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdSanitario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProdSanitario', models.CharField(default='Padrao', max_length=100)),
                ('loteProdSanitario', models.CharField(default='Padrao', max_length=100)),
                ('valorProdSanitario', models.FloatField(default='0.0')),
                ('dataCompraProdSanitario', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
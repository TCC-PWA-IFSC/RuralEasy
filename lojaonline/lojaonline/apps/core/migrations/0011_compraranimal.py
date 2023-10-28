# Generated by Django 4.2 on 2023-08-10 12:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_venda'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprarAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataComprarAnimal', models.DateField(default=datetime.date.today)),
                ('valorComprarAnimal', models.FloatField(default='0.0')),
                ('observacoesComprarAnimal', models.CharField(default='Padrao', max_length=100)),
                ('idComprarAnimal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.animal')),
            ],
        ),
    ]

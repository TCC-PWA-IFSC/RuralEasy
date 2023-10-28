# Generated by Django 4.2 on 2023-08-14 12:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_ocorrencias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inseminacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInseminacao', models.DateField(default=datetime.date.today)),
                ('horaCio', models.CharField(default='Padrao', max_length=100)),
                ('tecnica', models.CharField(default='Padrao', max_length=100)),
                ('diaGestacao', models.DateField(default=datetime.date.today)),
                ('idInseminador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.veterinario')),
                ('idTouro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.animal')),
            ],
        ),
    ]
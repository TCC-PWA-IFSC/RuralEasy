# Generated by Django 4.2 on 2023-10-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_lote_tipocultivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='outradespesa',
            name='motivoGasto',
            field=models.CharField(default='Padrao', max_length=100),
        ),
    ]

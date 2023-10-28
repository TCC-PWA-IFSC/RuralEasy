# Generated by Django 4.2 on 2023-05-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221003_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutorRural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProd', models.CharField(max_length=100)),
                ('cpf', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropriedadeRural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProp', models.CharField(max_length=100)),
                ('produtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produtorrural')),
            ],
        ),
    ]
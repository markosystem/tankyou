# Generated by Django 2.1.7 on 2019-04-11 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tankyou', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(max_length=7, verbose_name='Número da Placa'),
        ),
    ]
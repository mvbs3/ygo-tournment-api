# Generated by Django 5.1.2 on 2025-01-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneio', '0006_alter_torneio_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneio',
            name='identificador',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='categoriatorneio',
            name='titulo',
            field=models.CharField(choices=[('L', 'Local'), ('OTS', 'OTS - Championship'), ('R', 'Remote Duel'), ('P', 'Modelo Personalizado')], max_length=3),
        ),
    ]
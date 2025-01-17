# Generated by Django 5.1.2 on 2025-01-09 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duelists', '0004_alter_duelist_nickname'),
        ('torneio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1_matches', to='duelists.duelist')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2_matches', to='duelists.duelist')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneio.torneio')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to='duelists.duelist')),
            ],
        ),
    ]

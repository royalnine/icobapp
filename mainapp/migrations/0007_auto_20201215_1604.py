# Generated by Django 3.1.4 on 2020-12-15 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20201215_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(related_name='matches', to='mainapp.Player'),
        ),
        migrations.AlterField(
            model_name='playervote',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_votes', to='mainapp.match'),
        ),
        migrations.AlterField(
            model_name='playervote',
            name='player_voted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_by_player', to='mainapp.player'),
        ),
        migrations.AlterField(
            model_name='playervote',
            name='player_voted_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_for_player', to='mainapp.player'),
        ),
    ]

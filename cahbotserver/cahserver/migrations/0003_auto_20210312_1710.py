# Generated by Django 3.1.7 on 2021-03-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cahserver', '0002_auto_20210310_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamegroup',
            name='players',
            field=models.ManyToManyField(blank=True, to='cahserver.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='total_wons',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreentry',
            name='matchs_won',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreentry',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]

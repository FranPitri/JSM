# Generated by Django 2.2.1 on 2019-06-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayofweek',
            name='name',
            field=models.CharField(max_length=16, unique=True, verbose_name='Dia de la semana'),
        ),
    ]

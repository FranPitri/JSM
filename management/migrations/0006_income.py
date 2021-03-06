# Generated by Django 2.2.1 on 2019-06-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_son'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64, verbose_name='Tipo de ingreso')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='is_working',
            field=models.BooleanField(default=False, verbose_name='Trabaja'),
        ),
        migrations.AddField(
            model_name='person',
            name='note',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='person',
            name='work_place',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Lugar de trabajo'),
        ),
        migrations.AddField(
            model_name='person',
            name='income',
            field=models.ManyToManyField(blank=True, related_name='person', to='management.Income'),
        ),
    ]

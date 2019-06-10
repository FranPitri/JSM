# Generated by Django 2.2.1 on 2019-06-09 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0012_add_education_stage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Nombre de la actividad')),
                ('start_date', models.DateField(verbose_name='Comienzo de la actividad')),
                ('end_date', models.DateField(verbose_name='Fin de la actividad')),
                ('student', models.ManyToManyField(related_name='activities', to='management.Person')),
                ('teacher', models.ManyToManyField(related_name='activities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Dia de la semana')),
            ],
            options={
                'verbose_name': 'Dias de la semana',
            },
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Hora de inicio de la actividad')),
                ('end_time', models.TimeField(verbose_name='Hora de end de la actividad')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turns', to='management.Activity')),
                ('day_of_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='management.DayOfWeek')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='management.Activity')),
                ('assistance', models.ManyToManyField(related_name='courses', to='management.Person')),
            ],
            options={
                'verbose_name': 'Asistencia',
                'verbose_name_plural': 'Asistencias',
            },
        ),
    ]
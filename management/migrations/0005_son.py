# Generated by Django 2.2.1 on 2019-06-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_vcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Son',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=128, verbose_name='Apellido')),
                ('parent', models.ManyToManyField(related_name='sons', to='management.Person')),
            ],
            options={
                'verbose_name': 'Hijo',
                'verbose_name_plural': 'Hijos',
            },
        ),
    ]
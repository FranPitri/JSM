# Generated by Django 2.2.1 on 2019-06-08 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=128, verbose_name='Apellido')),
                ('address', models.ManyToManyField(blank=True, related_name='relative', to='management.Address')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='civil_status',
            field=models.IntegerField(choices=[(0, 'Soltero/a'), (1, 'Casado/a'), (2, 'Divorciado/a'), (4, 'Viudo/a')], default=0, verbose_name='Estado civil'),
        ),
        migrations.CreateModel(
            name='Sibling',
            fields=[
                ('relative_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.Relative')),
                ('date_of_birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sibling', to='management.Person')),
            ],
            options={
                'verbose_name': 'Hermano',
                'verbose_name_plural': 'Hermanos',
            },
            bases=('management.relative',),
        ),
        migrations.CreateModel(
            name='ResponsibleFamily',
            fields=[
                ('relative_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.Relative')),
                ('type', models.IntegerField(choices=[(0, 'Padre'), (0, 'Madre'), (0, 'Tutor')], default=0, verbose_name='Familiar')),
                ('is_alive', models.BooleanField(default=True, verbose_name='Esta vivo')),
                ('work', models.CharField(blank=True, max_length=64, null=True, verbose_name='Ocupación')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsible_family', to='management.Person')),
            ],
            options={
                'verbose_name': 'Familiar responble',
                'verbose_name_plural': 'Familiares responbles',
            },
            bases=('management.relative',),
        ),
    ]

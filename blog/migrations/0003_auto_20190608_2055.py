# Generated by Django 2.2.1 on 2019-06-08 20:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190608_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='skere', verbose_name='Contenido'),
            preserve_default=False,
        ),
    ]

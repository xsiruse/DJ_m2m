# Generated by Django 2.1.1 on 2019-12-26 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20191226_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationship',
            options={'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ['name'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]

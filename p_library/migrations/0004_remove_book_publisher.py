# Generated by Django 2.2.6 on 2019-11-11 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20191111_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
    ]

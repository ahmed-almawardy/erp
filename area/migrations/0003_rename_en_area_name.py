# Generated by Django 3.2 on 2021-06-20 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_auto_20210620_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='en',
            new_name='name',
        ),
    ]

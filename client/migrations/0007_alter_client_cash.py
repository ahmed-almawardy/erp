# Generated by Django 3.2 on 2021-06-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_client_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cash',
            field=models.IntegerField(blank=True, default=0.0, null=True, verbose_name='inital cash of account'),
        ),
    ]
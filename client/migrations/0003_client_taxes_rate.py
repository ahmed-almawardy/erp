# Generated by Django 3.2 on 2021-05-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='taxes_rate',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='Taxes Rate'),
        ),
    ]

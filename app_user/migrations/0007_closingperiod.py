# Generated by Django 3.2 on 2021-06-08 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_auto_20210603_1253'),
        ('client', '0005_auto_20210603_1253'),
        ('app_user', '0006_user_addtional_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosingPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.IntegerField(verbose_name='cash')),
                ('day', models.DateTimeField(verbose_name='date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='peroid', to='client.client', verbose_name='Client')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='peroid', to='supplier.supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Closing Period',
                'verbose_name_plural': 'Closing Period',
            },
        ),
    ]

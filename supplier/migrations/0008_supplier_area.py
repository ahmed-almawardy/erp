# Generated by Django 3.2 on 2021-06-20 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0004_alter_area_options'),
        ('supplier', '0007_alter_supplier_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='area.area', verbose_name='Area'),
            preserve_default=False,
        ),
    ]
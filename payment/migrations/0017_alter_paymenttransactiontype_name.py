# Generated by Django 3.2 on 2021-06-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0016_alter_paymenttransactiontype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttransactiontype',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Payment Type'),
        ),
    ]
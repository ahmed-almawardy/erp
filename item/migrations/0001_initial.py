# Generated by Django 3.2 on 2021-05-23 13:23

import _helpers.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CTX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'CTX',
                'verbose_name_plural': 'CTX',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(choices=[(1, 'Fixed'), (2, 'Precentage')], default=1, verbose_name='Type')),
                ('amount', models.IntegerField(default=0, verbose_name='Rate')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250, verbose_name='Label')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('price', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price of an item')),
                ('details', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('unit', models.IntegerField(choices=[(1, 'M'), (2, 'G')], default=1, verbose_name='Unit')),
                ('image', models.ImageField(blank=True, null=True, upload_to=_helpers.models.product_img_upload_path, verbose_name='Image')),
                ('banner', models.ImageField(blank=True, null=True, upload_to=_helpers.models.product_banner_upload_path, verbose_name='Banner')),
                ('tax', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Tax')),
                ('serial_no', models.IntegerField(default=0, verbose_name='Serial Number')),
                ('supplier_price', models.FloatField(default=0.0, verbose_name='Supplier price')),
                ('note', models.TextField(default='item ...', verbose_name='Desctiption')),
                ('optional', models.BooleanField(default=False, verbose_name='Is optional')),
                ('data', models.JSONField(blank=True, null=True, verbose_name='Item as Json')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='ItemFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50, verbose_name='Filename')),
                ('path', models.CharField(max_length=50, verbose_name='Path')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Number')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('label', models.CharField(max_length=250, verbose_name='Display Name')),
            ],
        ),
        migrations.CreateModel(
            name='Vat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='Number')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('label', models.CharField(max_length=250, verbose_name='Display Name')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='item.category', verbose_name='Category')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='item.option', verbose_name='Option')),
            ],
            options={
                'verbose_name': 'Variation',
                'verbose_name_plural': 'Variations',
            },
        ),
        migrations.CreateModel(
            name='SupplierItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('note', models.TextField(default='...', verbose_name='Desctiption')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='item.item', verbose_name='Item')),
            ],
        ),
    ]

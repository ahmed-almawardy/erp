# Generated by Django 3.2 on 2021-05-31 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_auto_20210531_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Payment Type')),
                ('transaction_for', models.IntegerField(choices=[(1, 'Debit'), (2, 'Credit')], verbose_name='which type is related')),
            ],
        ),
        migrations.RemoveField(
            model_name='clientpaymenttransaction',
            name='payment_type',
        ),
        migrations.RemoveField(
            model_name='supplierpaymenttransaction',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'Debit'), (2, 'Credit')], default=1, help_text='the transaction type', verbose_name='Payment transaction Type'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='currency',
            field=models.IntegerField(choices=[(1, 'egp')], default=1, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='currency',
            field=models.IntegerField(choices=[(1, 'egp')], default=1, help_text='currency of transaction', verbose_name='Currency'),
        ),
        migrations.DeleteModel(
            name='PaymentType',
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='type_tranasction',
            field=models.ForeignKey(help_text='transaction type', on_delete=django.db.models.deletion.DO_NOTHING, to='payment.paymenttransactiontype', verbose_name='Transaction type'),
        ),
    ]

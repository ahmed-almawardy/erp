# Generated by Django 3.2 on 2021-06-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0005_alter_user_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addtional_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Addtional User Phone Number'),
        ),
    ]

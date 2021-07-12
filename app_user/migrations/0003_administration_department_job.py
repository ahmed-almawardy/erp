# Generated by Django 3.2 on 2021-06-06 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_auto_20210530_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Administration',
                'verbose_name_plural': 'Administrations',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('administration', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_user.administration', verbose_name='Administrattion')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Job')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_user.department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
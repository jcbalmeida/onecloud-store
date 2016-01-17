# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('v_cpu', models.IntegerField()),
                ('memory', models.FloatField()),
                ('disk_space', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OsFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServerPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computing.Provider')),
            ],
        ),
        migrations.AddField(
            model_name='operatingsystem',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='computing.OsFamily'),
        ),
    ]

# Generated by Django 2.1 on 2018-08-12 18:58

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, validators=[django.core.validators.DecimalValidator]), size=2), blank=True, default=list, size=None)),
                ('length', models.FloatField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='route',
            index=models.Index(fields=['-length'], name='tracker_rou_length_15686e_idx'),
        ),
    ]

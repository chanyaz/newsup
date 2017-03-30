# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0010_hindi_agra_hindi_ahmedabad_hindi_ajmer_hindi_aligarh_hindi_allahabad_hindi_almorah_hindi_alwar_hindi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hindi_Auto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cluster_Id', models.IntegerField(db_index=True)),
                ('URL', models.URLField(max_length=300)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Is_Rep', models.BooleanField(default=False)),
                ('Article', models.ForeignKey(to='newsApp.News_Article')),
                ('Source', models.ForeignKey(to='newsApp.News_Source')),
            ],
        ),
        migrations.CreateModel(
            name='Hindi_Crime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cluster_Id', models.IntegerField(db_index=True)),
                ('URL', models.URLField(max_length=300)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Is_Rep', models.BooleanField(default=False)),
                ('Article', models.ForeignKey(to='newsApp.News_Article')),
                ('Source', models.ForeignKey(to='newsApp.News_Source')),
            ],
        ),
    ]

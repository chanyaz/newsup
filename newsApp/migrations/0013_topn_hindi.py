# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0012_hindi_faridabad'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopN_Hindi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('URL', models.URLField(max_length=300)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Article', models.ForeignKey(to='newsApp.News_Article')),
                ('Source', models.ForeignKey(to='newsApp.News_Source')),
            ],
        ),
    ]

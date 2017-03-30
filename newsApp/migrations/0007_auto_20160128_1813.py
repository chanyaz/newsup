# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0006_auto_20160128_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Feed1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('URL', models.URLField(max_length=500)),
                ('Type', models.CharField(default=b'RSS 2.0', max_length=20)),
                ('Category', models.ForeignKey(to='newsApp.News_Category')),
                ('Language', models.ForeignKey(to='newsApp.Language')),
                ('Source', models.ForeignKey(to='newsApp.News_Source')),
            ],
        ),
        migrations.AlterField(
            model_name='news_feed',
            name='URL',
            field=models.URLField(max_length=500),
        ),
    ]

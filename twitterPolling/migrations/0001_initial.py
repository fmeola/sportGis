# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('toponimo_i', models.IntegerField()),
                ('nombre', models.CharField(max_length=254)),
                ('link', models.CharField(max_length=254)),
                ('varones', models.FloatField()),
                ('mujeres', models.FloatField()),
                ('tot_pob', models.FloatField()),
                ('hogares', models.FloatField()),
                ('viv_part', models.FloatField()),
                ('viv_part_h', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]

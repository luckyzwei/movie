# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviedetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('totle_title', models.CharField(max_length=200)),
                ('directors', models.CharField(max_length=200)),
                ('bianjus', models.CharField(max_length=200)),
                ('actors', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('titlepic', models.CharField(max_length=200)),
                ('qingxi', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('uptime', models.CharField(max_length=200)),
                ('timelen', models.CharField(max_length=200)),
                ('altername', models.CharField(max_length=200)),
                ('doubanscore', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('piclist', models.CharField(max_length=500)),
                ('baiduyunlink', models.CharField(max_length=200)),
                ('baiduyunpwd', models.CharField(max_length=50)),
                ('magnetlist', models.CharField(max_length=500)),
                ('createtime', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'detail',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='moviehot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(to='movie.moviedetail')),
            ],
            options={
                'db_table': 'hot',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='movietop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('picurl', models.CharField(max_length=500)),
                ('movieurl', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'top',
            },
            bases=(models.Model,),
        ),
    ]

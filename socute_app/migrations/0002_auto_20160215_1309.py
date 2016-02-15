# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socute_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('header', models.TextField()),
                ('text', models.TextField()),
                ('expire_time', models.DateField()),
                ('public', models.BooleanField(default=True)),
                ('write', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=500)),
                ('salt', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='textmodel',
            name='owner',
            field=models.ForeignKey(null=True, to='socute_app.UserModel'),
        ),
    ]

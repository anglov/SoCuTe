# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socute_app', '0002_auto_20160215_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, to='socute_app.UserModel'),
        ),
    ]

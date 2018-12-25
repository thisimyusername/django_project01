# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=256)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-register_date'],
            },
        ),
    ]

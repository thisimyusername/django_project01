# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20181222_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=256)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '确认码',
                'verbose_name_plural': '确认码',
                'ordering': ['-register_date'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='confirmstring',
            name='user',
            field=models.OneToOneField(to='login.User'),
        ),
    ]

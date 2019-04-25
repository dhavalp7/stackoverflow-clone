# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 04:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptAnswer',
            fields=[
                ('acceptedansid', models.AutoField(primary_key=True, serialize=False)),
                ('ansid', models.ForeignKey(blank=True, db_column='ansid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Answer')),
                ('queid', models.ForeignKey(blank=True, db_column='queid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Question')),
                ('userid', models.ForeignKey(blank=True, db_column='userid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'acceptedanswer',
                'managed': True,
            },
        ),
    ]
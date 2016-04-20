# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ccType', models.CharField(max_length=20)),
                ('ccNumber', models.CharField(max_length=16)),
                ('expDate', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('status', models.CharField(default=b'Silver', max_length=10)),
                ('credits', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

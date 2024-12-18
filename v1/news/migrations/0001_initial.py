# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 14:17
from __future__ import unicode_literals

from django.db import migrations, models

from v1.common.db_fields import AutoSlugField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191, unique=True, verbose_name='title')),
                ('slug', AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('frontpage', models.BooleanField(default=False, help_text='determines if the story appears on the front page', verbose_name='frontpage')),
                ('image', models.ImageField(blank=True, upload_to='uploads/news/', verbose_name='image')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]

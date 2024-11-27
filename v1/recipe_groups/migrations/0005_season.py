# Generated by Django 4.2.16 on 2024-11-21 13:08

from django.db import migrations, models
import v1.common.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_groups', '0004_auto_20220514_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('slug', v1.common.db_fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug')),
            ],
        ),
    ]

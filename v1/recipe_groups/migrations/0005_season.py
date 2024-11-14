# Generated by Django 4.2.16 on 2024-11-14 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import v1.common.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe_groups', '0004_auto_20220514_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('slug', v1.common.db_fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

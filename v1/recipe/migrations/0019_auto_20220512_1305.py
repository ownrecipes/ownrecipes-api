# Generated by Django 2.1.7 on 2022-05-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0018_remove_subrecipe_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='source',
            field=models.CharField(blank=True, max_length=200, verbose_name='source'),
        ),
    ]
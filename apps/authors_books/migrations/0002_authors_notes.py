# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-16 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors_books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='Author created before field'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-25 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0005_wish_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='granted_wishes',
            field=models.ManyToManyField(related_name='wishes_granted', to='belt.User'),
        ),
        migrations.AddField(
            model_name='wish',
            name='pending_wishes',
            field=models.ManyToManyField(related_name='wishes_pending', to='belt.User'),
        ),
        migrations.AlterField(
            model_name='wish',
            name='liked_by',
            field=models.ManyToManyField(default='0', related_name='liked_wishes', to='belt.User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0006_auto_20160408_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation_vl',
            name='content_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='annotation_vl',
            name='distance',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='annotation_vl',
            name='fear',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='annotation_vl',
            name='humor_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='annotation_vl',
            name='source',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='hashtags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='reply_to_user',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='reply_to_user_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweet_to_user',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweet_to_user_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

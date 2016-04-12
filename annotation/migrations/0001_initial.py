# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation_eb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotation_id', models.BigIntegerField()),
                ('tweet_id', models.BigIntegerField()),
                ('student_id', models.BigIntegerField()),
                ('is_filled', models.BooleanField(default=False)),
                ('humor_type', models.CharField(blank=True, max_length=50, null=True)),
                ('distance', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('content_type', models.CharField(blank=True, max_length=50, null=True)),
                ('fear', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Annotation_vl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotation_id', models.BigIntegerField()),
                ('tweet_id', models.BigIntegerField()),
                ('student_id', models.BigIntegerField()),
                ('is_filled', models.BooleanField(default=False)),
                ('humor_type', models.CharField(blank=True, max_length=50, null=True)),
                ('distance', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('content_type', models.CharField(blank=True, max_length=50, null=True)),
                ('attitude', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField()),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('reply_to_user', models.BigIntegerField(blank=True, null=True)),
                ('reply_to_user_url', models.CharField(blank=True, max_length=255, null=True)),
                ('retweet_to_user', models.BigIntegerField(blank=True, null=True)),
                ('retweet_to_user_url', models.CharField(blank=True, max_length=255, null=True)),
                ('user_name', models.CharField(max_length=255, null=True)),
                ('user_followers', models.BigIntegerField(null=True)),
                ('user_location', models.CharField(blank=True, max_length=255, null=True)),
                ('tweet_location', models.CharField(blank=True, max_length=255, null=True)),
                ('hashtags', models.CharField(blank=True, max_length=255, null=True)),
                ('tweet_url', models.CharField(max_length=255, null=True)),
                ('tweet_text', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='annotation_vl',
            unique_together=set([('tweet_id', 'student_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotation_eb',
            unique_together=set([('tweet_id', 'student_id')]),
        ),
    ]

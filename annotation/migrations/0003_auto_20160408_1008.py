# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0002_auto_20160408_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='annotation_vl',
            name='content_type',
            field=models.CharField(choices=[(1, 'FirstHand'), (2, 'SecondHand'), (3, 'RequestingHelp'), (4, 'CoordinatingRelief'), (5, 'ProvidingCounseling'), (6, 'CritiziseGovernement'), (7, 'Memorializing'), (8, 'DiscussCauses'), (9, 'ReconnectingMembers'), (10, 'Misc')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='annotation_vl',
            name='distance',
            field=models.CharField(choices=[(1, 'WestAfrika'), (2, 'Afrika'), (3, 'Europa'), (4, 'Nederland'), (5, 'NoordAmerika'), (6, 'OverigGeen')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='annotation_vl',
            name='fear',
            field=models.CharField(choices=[(1, 'Jezelf'), (2, 'Anderen'), (3, 'JezelfAnderen'), (4, 'Geen')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='annotation_vl',
            name='source',
            field=models.CharField(choices=[(1, 'Overheid'), (2, 'Journalistiek'), (3, 'Burger'), (4, 'Beroemdheid'), (5, 'Instantie'), (6, 'Overig')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='annotation_vl',
            name='humor_type',
            field=models.CharField(choices=[(1, 'Anekdote'), (2, 'Fantasie'), (3, 'Belediging'), (4, 'Ironie'), (5, 'Grap'), (6, 'Observatief'), (7, 'Quote'), (8, 'Rollenspel'), (9, 'Zelfspot'), (10, 'Vulgariteit'), (11, 'Woordspeling'), (12, 'Overig'), (13, 'Geen')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='annotation_vl',
            name='student_id',
            field=models.ForeignKey(default=621142, on_delete=django.db.models.deletion.CASCADE, to='annotation.Student'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockOfSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='skills',
            new_name='skill_list',
        ),
        migrations.AlterField(
            model_name='picture',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic_list', to='main.Project'),
        ),
        migrations.AddField(
            model_name='blockofskill',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_skill_list', to='main.Project'),
        ),
        migrations.AddField(
            model_name='blockofskill',
            name='skill_list',
            field=models.ManyToManyField(to='main.Skill'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-11 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0069_auto_20161107_1932'),
        ('materia', '0068_auto_20161110_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoproposicao',
            name='perfis',
            field=models.ManyToManyField(blank=True, to='compilacao.PerfilEstruturalTextoArticulado', verbose_name='Perfis Estruturais de Textos Articulados'),
        ),
    ]

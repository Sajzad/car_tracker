# Generated by Django 3.2.11 on 2022-01-20 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_operator_is_first'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operator',
            name='is_first',
        ),
    ]

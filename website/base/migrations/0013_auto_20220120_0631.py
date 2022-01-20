# Generated by Django 3.2.11 on 2022-01-20 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_operator_is_first'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='lng',
        ),
        migrations.CreateModel(
            name='LatLong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=5, default=0, max_digits=5)),
                ('lng', models.DecimalField(decimal_places=5, default=0, max_digits=5)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.assignment')),
            ],
        ),
    ]
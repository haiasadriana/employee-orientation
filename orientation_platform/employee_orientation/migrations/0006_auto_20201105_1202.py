# Generated by Django 3.1.3 on 2020-11-05 12:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_orientation', '0005_auto_20201103_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='assigned_project',
            field=models.ForeignKey(blank='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_orientation.project'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(blank='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employeetraining',
            name='percentage',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='employeetraining',
            name='start_date',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]

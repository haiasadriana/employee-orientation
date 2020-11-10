# Generated by Django 3.1.3 on 2020-11-03 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_orientation', '0003_auto_20201103_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='assigned_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_orientation.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='training_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_orientation.training'),
        ),
    ]
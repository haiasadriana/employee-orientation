# Generated by Django 3.1.3 on 2020-11-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_orientation', '0010_auto_20201112_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmaterial',
            name='material_resource',
            field=models.FileField(upload_to=''),
        ),
    ]

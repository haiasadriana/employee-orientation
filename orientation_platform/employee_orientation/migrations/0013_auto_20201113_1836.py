# Generated by Django 3.1.3 on 2020-11-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_orientation', '0012_auto_20201113_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmaterial',
            name='material_resource',
            field=models.FileField(upload_to='training_materials/'),
        ),
    ]

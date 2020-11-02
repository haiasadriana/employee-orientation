from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Training(models.Model):
    TRAINING_STATUS = (
        ('PEND', 'PENDING'),
        ('NOW','IN PROGRESS'),
        ('DONE','COMPLETED')
    )
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    training_status = models.CharField(choices=TRAINING_STATUS, max_length=4)

class TrainingMaterial(models.Model):
    name = models.CharField(max_length=128)
    material_resource = models.BinaryField()
    training_name = models.ForeignKey(Training, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)
    training_name = models.ForeignKey(Training, on_delete=models.CASCADE)


class Employee(AbstractUser):
    assigned_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=50)
    trainings = models.ManyToManyField(Training, through="EmployeeTraining")

class EmployeeTraining(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    percentage = models.FloatField()



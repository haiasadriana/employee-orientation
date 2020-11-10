from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .project import Project
from .training import Training


class Employee(AbstractUser):
    ROLE = (
        ('TRAINEE', 'TRAINEE'),
        ('MENTOR', 'MENTOR')
    )
    assigned_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    employee_role = models.CharField(choices=ROLE, max_length=10, null=True)
    trainings = models.ManyToManyField(Training, through="EmployeeTraining")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.employee_role}"


class EmployeeTraining(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    start_date = models.DateTimeField(timezone.now)
    end_date = models.DateTimeField(null=True)
    percentage = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

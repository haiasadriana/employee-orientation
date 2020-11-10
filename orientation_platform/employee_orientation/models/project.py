from django.db import models
from django.utils import timezone
from .training import Training


class Project(models.Model):
    name = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    end_date = models.DateTimeField(null=True)
    training_name = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

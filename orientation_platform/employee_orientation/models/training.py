from django.db import models
from django.utils import timezone


class Training(models.Model):
    TRAINING_STATUS = (
        ('PEND', 'PENDING'),
        ('NOW', 'IN PROGRESS'),
        ('DONE', 'COMPLETED')
    )
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    training_status = models.CharField(choices=TRAINING_STATUS, max_length=4)

    def __str__(self):
        return self.name


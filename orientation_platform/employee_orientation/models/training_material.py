from django.db import models
from .training import Training


class TrainingMaterial(models.Model):
    name = models.CharField(max_length=128)
    material_resource = models.BinaryField()
    training_name = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

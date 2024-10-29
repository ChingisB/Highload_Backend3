from django.db import models

# Create your models here.
class KeyValuePropertyModel(models.Model):
    key = models.CharField(max_length=20, unique=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}:{self.value}"
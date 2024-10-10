from typing import Any
from django.db import models
import os

class LottiImage(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.image.name
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        return super().delete(*args, **kwargs)
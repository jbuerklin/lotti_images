from typing import Any
from django.db import models
import os
import hashlib

class LottiImage(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hash = models.CharField(max_length=64, default="", unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.image.name
        if self.image and not self.hash:
            self.hash = hashlib.md5(self.image.read()).hexdigest()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        return super().delete(*args, **kwargs)

from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=2000)
    created_at = models.DateTimeField(datetime.now(), blank=True)

    def __str__(self):
        return self.title

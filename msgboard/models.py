# from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone


class Message(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

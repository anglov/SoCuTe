from django.db import models


class TextModel(models.Model):
    text = models.TextField()

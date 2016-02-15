from django.db import models

class TextModel(models.Model):
    header = models.TextField()
    text = models.TextField()
    owner = models.ForeignKey('UserModel', null=True, blank=True)
    expire_time = models.DateField()
    public = models.BooleanField(default=True)


class UserModel(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=500)
    salt = models.CharField(max_length=50)
    is_active = models.BooleanField()


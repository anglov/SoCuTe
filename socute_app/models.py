from django.db import models

class TextModel(models.Model):
    header = models.TextField()
    text = models.TextField()
    owner = models.ForeignKey('UserModel', null=False)
    expire_time = models.DateField(auto_now_add=True)
    public = models.BooleanField()
    write = models.BooleanField()


class UserModel(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=500)
    salt = models.CharField(max_length=50)
    is_active = models.BooleanField()


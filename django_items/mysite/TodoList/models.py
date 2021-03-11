from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    list_item = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.list_item

class MainList(models.Model):
    list_main = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

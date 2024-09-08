from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=245)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=245)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    count = models.PositiveIntegerField()

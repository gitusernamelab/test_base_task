from django.db import models
import uuid


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

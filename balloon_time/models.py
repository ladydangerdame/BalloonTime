from django.db import models

# Create your models here.

class Party(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Clown(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

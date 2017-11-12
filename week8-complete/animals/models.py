from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.TextField(max_length=30, unique=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=60)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=60)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.author + ": " + self.text

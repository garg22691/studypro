from django.db import models

# Create your models here.

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

class Answers(models.Model):
    Answers = models.TextField()
    vote = models.IntegerField()
    questionid = models.IntegerField()
    

class companies(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Topic(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"


class category(models.Model):
    name = models.CharField(max_length=64)
    topic = models.ManyToManyField(Topic, blank=True, related_name="categories")
    companies = models.ManyToManyField(companies, blank=True, related_name="categories")
    def __str__(self):
        return f"{self.name}"

class Questions(models.Model):
    Question = models.TextField()
    category = models.ManyToManyField(category, blank=True, related_name="questions")
    vote = models.IntegerField()
    def __str__(self):
        return f"{self.Question}"




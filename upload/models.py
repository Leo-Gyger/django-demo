import datetime

from django.db import models


class Question(models.Model):
    text: str = models.CharField(max_length=200)
    date: datetime = models.DateTimeField('date published')

    def __str__(self):
        return self.text


class Choice(models.Model):

    def __str__(self):
        return self.choice

    question: Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice: str = models.CharField(max_length=200)
    votes: int = models.IntegerField(default=0)

# qa/models.py
from django.db import models

# Create your models here.
class InputType(models.Model):
    name = models.CharField(max_length=8)
    #text, radio, checkbox, date, time

class Question(models.Model):
    input_type = models.ForeignKey(InputType, on_delete=models.CASCADE)
    text       = models.CharField(max_length=255)

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text        = models.CharField(max_length=255)

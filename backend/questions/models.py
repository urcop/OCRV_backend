from uuid import uuid4

from django.db import models


class Skills(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(max_length=255)


class Question(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    complexity = models.PositiveSmallIntegerField(default=0)
    is_many = models.BooleanField(default=False)
    question = models.CharField(max_length=255)
    variants = models.JSONField()
    answer = models.JSONField()



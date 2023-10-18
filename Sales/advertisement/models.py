from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=40)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, name='rubric')


class Rubric(models.Model):
    name = models.CharField(max_length=20)
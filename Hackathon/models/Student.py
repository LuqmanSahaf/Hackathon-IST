from django.db import models

from . import Person


class Student(Person):
    fruit = models.CharField(max_length=32)

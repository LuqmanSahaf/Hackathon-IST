from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=32, null=False, default='')
    code = models.CharField(max_length=8, default=None)

    students = models.ManyToManyField(through='GroupStudent',
                                      to='Hackathon.Student',
                                      verbose_name='list of students')

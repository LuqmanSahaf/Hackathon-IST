from django.db import models


class Student(models.Model):
    fruit = models.CharField(max_length=32)

    groups = models.ManyToManyField('Hackathon.Group',
                                    through='Hackathon.GroupStudent',
                                    verbose_name='list of groups')

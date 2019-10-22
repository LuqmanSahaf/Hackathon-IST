from django.db import models


class GroupStudent(models.Model):
    group = models.ForeignKey('Hackathon.Group', on_delete=models.CASCADE, null=False)
    student = models.ForeignKey('Hackathon.Student', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "group_x_student"
        unique_together = [
            ['group', 'student']
        ]

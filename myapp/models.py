from django.db import models

# Create your models here.
class Students(models.Model):
    firstname=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    student_id=models.IntegerField()
    course=models.CharField(max_length=20)

    def __str__(self):
        return (f'Studient ID: {self.id} Firstname : {self.firstname}'
                f'Surname :{self.surname} Student ID{self.student_id}'
                f'Course: {self.course}')
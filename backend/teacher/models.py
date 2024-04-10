from django.db import models
from core_app.models import Student,Teacher
from academics.models import Section,Grade,ClassSubject


class Exam(models.Model):
    description = models.TextField()
    details = models.ForeignKey(ClassSubject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.description



class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}'s result for {self.exam.description}"

    
class Task(models.Model):
    HOMEWORK = 'homework'
    ASSIGNMENT = 'assignment'
    TYPE_CHOICES = [
        (HOMEWORK, 'Homework'),
        (ASSIGNMENT, 'Assignment'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    details = details = models.ForeignKey(ClassSubject , on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):  
        return self.title
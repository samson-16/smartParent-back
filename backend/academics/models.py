from django.db import models
from core_app.models import Teacher

class Grade(models.Model):
    grade = models.CharField(max_length=10 , unique=True)

    def __str__(self):
        return self.grade

class Section(models.Model):
    section = models.CharField(max_length=10)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('grade', 'section')
    def __str__(self):
        return f"{self.grade} - {self.section}"

class Subject(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class ClassSubject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('grade', 'section', 'subject', 'teacher')
        
    def __str__(self):
        return f"{self.grade} - {self.section} - {self.subject}"



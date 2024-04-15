from rest_framework import serializers
from .models import Task, Exam, ExamResult, Resource
from academics.serializers import ClassSubjectSerializer , ListClassSubjectSerializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskListSerializer(serializers.ModelSerializer):
    details = ListClassSubjectSerializer()
    class Meta:
        model = Task
        fields = ['id' , 'title' , 'description' , 'details' , 'date' , 'deadline', 'type',]


class ExamSerializer(serializers.ModelSerializer):
    details = ListClassSubjectSerializer()
    class Meta:
        model = Exam
        fields = ['id' , 'description' , 'exam_date' , 'total_marks' , 'grade' , 'details']

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['id' , 'exam' , 'description', 'teacher', 'file' ]

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'title', 'grade', 'subject', 'file']

from rest_framework import serializers
from .models import Grade, Section, Subject, ClassSubject
from core_app.serializers import TeacherSerializer


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'grade']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'section', 'grade']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject']

class ClassSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSubject
        fields = ['id', 'grade', 'section', 'subject', 'teacher']

class ListClassSubjectSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
    section = SectionSerializer()
    subject = SubjectSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = ClassSubject
        fields = ['id', 'grade', 'section', 'subject', 'teacher']
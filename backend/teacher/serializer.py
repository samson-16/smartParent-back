from rest_framework import serializers
from .models import ExamResult,Assignment

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assignment
        fields = '__all__'
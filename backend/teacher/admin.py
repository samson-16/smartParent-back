# academics/admin.py

from django.contrib import admin
from .models import Exam, ExamResult, Task, Resource

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('description', 'exam_date', 'grade', 'total_marks')
    list_filter = ('grade', 'exam_date')
    search_fields = ('description', 'details__subject__subject', 'details__grade__grade')

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('description', 'exam', 'teacher')
    list_filter = ('exam__grade', 'teacher')
    search_fields = ('description', 'exam__description', 'teacher__name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'deadline', 'details', 'type')
    list_filter = ('details__grade', 'details__section', 'details__subject', 'type')
    search_fields = ('title', 'description', 'details__grade__grade', 'details__section__section', 'details__subject__subject')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade', 'subject')
    list_filter = ('grade', 'subject')
    search_fields = ('title', 'grade__grade', 'subject__subject')

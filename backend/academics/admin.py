# core_app/admin.py

from django.contrib import admin
from .models import Grade, Exam, Section, Subject, ClassSubject

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_filter = ('grade',)
    search_fields = ('section',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):
    list_filter = ('grade', 'section', 'subject', 'teacher') 
    search_fields = ('grade__grade', 'section__section', 'subject__subject', 'teacher__name') 

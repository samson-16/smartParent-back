from rest_framework import generics
from .models import Grade, Section, Subject, ClassSubject
from core_app.models import Student
from .serializers import GradeSerializer, SectionSerializer, SubjectSerializer, ClassSubjectSerializer , ListClassSubjectSerializer
from rest_framework.permissions import AllowAny
from core_app.serializers import StudentSerializer

class GradeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [AllowAny] 

class GradeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]

class SectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [AllowAny]

class SectionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [AllowAny]

class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]

class SubjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]

class ClassSubjectListAPIView(generics.ListAPIView):
    queryset = ClassSubject.objects.all()
    serializer_class = ListClassSubjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ClassSubject.objects.all()
        teacher = self.request.query_params.get('teacher')
        grade = self.request.query_params.get('grade')
        section = self.request.query_params.get('section')

        if teacher is not None:
            try:
                teacher = int(teacher)
                queryset = queryset.filter(teacher_id=teacher)
            except ValueError:
                pass

        if grade is not None:
            queryset = queryset.filter(grade__grade=grade)

        if section is not None:
            queryset = queryset.filter(section=section)

        return queryset


class ClassSubjectCreateAPIView(generics.CreateAPIView):
    queryset = ClassSubject.objects.all()
    serializer_class = ClassSubjectSerializer
    permission_classes = [AllowAny]

class ClassSubjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassSubject.objects.all()
    serializer_class = ClassSubjectSerializer
    permission_classes = [AllowAny]

class TeacherClassSubjectAPIView(generics.ListAPIView):
    serializer_class = ClassSubjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        teacher_id = self.kwargs.get('teacher_id')
        queryset = ClassSubject.objects.filter(teacher_id=teacher_id)
        return queryset

class StudentsBySectionListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        grade = self.request.query_params.get('grade')
        section = self.request.query_params.get('section')
        return Student.objects.filter(grade=grade, section=section)
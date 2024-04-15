from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core_app.models import Parent, Student
from teacher.models import Exam , ExamResult , Task
from academics.serializers import ListClassSubjectSerializer 
from academics.models import ClassSubject , Section , Grade
from teacher.serializers import TaskListSerializer, ExamSerializer, ExamResultSerializer
from core_app.serializers import ParentSerializer
from rest_framework.permissions import IsAuthenticated




class ParentDashboardAPIView(APIView):
    permission_classes =[IsAuthenticated]
    def get(self, request, parent_id):
        try:
            parent = Parent.objects.get(user__id=parent_id)
            children = parent.children.all()
            parent_serializer = ParentSerializer(parent)  
            
            parent_data = parent_serializer.data
            parent_data['children_data'] = []

            for child in children:
                grade = child.grade
                section_name = child.section
                section_obj = Section.objects.filter(section=section_name).first()

                grade_obj = Grade.objects.get(grade=grade)
                class_subjects = ClassSubject.objects.filter(grade=grade_obj, section=section_obj)
                tasks = Task.objects.filter(details__grade=grade_obj, details__section=section_obj).order_by('-date')
                exams = Exam.objects.filter(grade=grade_obj).order_by('-exam_date')
                exam_results = ExamResult.objects.filter(exam__grade=grade_obj)
                
                child_data = {
                    "child": f"{child.first_name} {child.last_name}",
                    "class_subjects": ListClassSubjectSerializer(class_subjects, many=True).data,
                    "tasks": TaskListSerializer(tasks, many=True).data,
                    "exams": ExamSerializer(exams, many=True).data,
                    "exam_results": ExamResultSerializer(exam_results, many=True).data
                }
                parent_data['children_data'].append(child_data)
                
            return Response(parent_data, status=status.HTTP_200_OK)
        except Parent.DoesNotExist:
            return Response({"error": "Parent not found"}, status=status.HTTP_404_NOT_FOUND)
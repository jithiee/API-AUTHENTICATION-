from django.shortcuts import render
from . models import Student
from .serializer import StudentSerializer
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

class StudentlListcCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentRetreveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
















# class StudentlList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
# class StudentlRetrive(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
# class StudentlDelete(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin ,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin
from . models import Student
from .serializer import StudentSerializer

# Create your views here.
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get (self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
   
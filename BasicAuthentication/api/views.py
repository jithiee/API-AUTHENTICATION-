from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from . models import Student
from . serializers import StudentSerializer



class StudentModelViewst(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer = StudentSerializer


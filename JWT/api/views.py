from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import Student
from .serializer import StudentSerializer
# from rest_framework.authentication import 
# from api.customAuth import CustomeAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class StudentModelView(ModelViewSet):
    queryset = Student.objects.all()
    serializer = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

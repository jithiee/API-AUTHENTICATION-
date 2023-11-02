from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer
from .models import Student
from rest_framework.authentication import BasicAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated ,IsAdminUser

# Create your views here.
class StudentModelViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    name = 'yassin'
    

    
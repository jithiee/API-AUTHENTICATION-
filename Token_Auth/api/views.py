from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from . serializer import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from . models import Student
from rest_framework.viewsets import ModelViewSet
from api.customAuth import CustomeAuthentication

class StundetModelvewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes =[CustomeAuthentication]
    permission_classes = [IsAuthenticated]

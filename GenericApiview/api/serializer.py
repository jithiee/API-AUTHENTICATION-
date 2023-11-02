from . models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    model = Student
    fields = ['id','name','roll','city']
    
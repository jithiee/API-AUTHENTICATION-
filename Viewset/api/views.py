from django.shortcuts import render
from rest_framework import viewsets
from . models import Student
from .serializer import StudentSerialiser
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.

class StudentViewset(viewsets.ViewSet):
    def list(self,request):
            stu = Student.objects.all()
            serializer = StudentSerialiser(stu,many =True)
            return Response(serializer.data)
    def retrieve(self,request,pk=None):
            try:
                if pk is not None:
                    stu = Student.objects.get(id = pk)
                    serializer = StudentSerialiser(stu)
                    return Response (serializer.data,status=status.HTTP_200_OK)
            except :
                return Response ( serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
            
    def create(self,request):
        try:
            deserializer = StudentSerialiser(data=request.data)
            if deserializer.is_valid():
                deserializer.save()
                return Response({'msg':'data created'},status=status.HTTP_201_CREATED) 
            return Response (deserializer.errors)
        except :
            raise Exception('invalid creation')
            # return Response({'msg':'smyhng wrg'},status=status.HTTP_400_BAD_REQUEST) 
            
    def update(self,request,pk = None):
            try:
                stu = Student.objects.get(id = pk)
                deserializer = StudentSerialiser(stu,request.data) 
                if deserializer.is_valid():
                    deserializer.save()
                    return Response({'msg':'complete  data updated'},status=status.HTTP_200_OK)
                return Response (deserializer.errors,status=status.HTTP_400_BAD_REQUEST)  
            except :
                raise Exception ('invalid update') 
    def partial_update(self ,request ,pk=None):
        stu = Student.objects.get(id = pk)
        deserializer = StudentSerialiser(stu,request.data ,partial = True)
        if deserializer.is_valid():
            deserializer.save()
            return Response({'msg':'partal update'})
        return Response(deserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg':'data deleted'})
    
    
        
         
                       
            
            
            
                    
            
                

      
        
    
        
        
    

from django.shortcuts import render
from . models import Student
from rest_framework.views import APIView
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class StudentApiView(APIView):
    def get(self , request ,pk =None, format = None):
        id = pk
        print(id,'hhhhhhhhjkslfdhlkheirfhi;')
        if id is not None:
            try:
                stu = Student.objects.get(id = id)
                request.session['kona']=stu
                serializer = StudentSerializer(stu)
                return Response(serializer.data)

            except ObjectDoesNotExist:
                return Response({'msg': 'Student not founddddddddddd'}, status=status.HTTP_404_NOT_FOUND)
            
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)
    
    
    
    def post (self,request,format =None):
        deserializer = StudentSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            kona = request.session.get('kona')
            print(kona)
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(deserializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    def put(self,request,pk=None,format =None):
      
        stu = Student.objects.get(id = pk)
        deserializer = StudentSerializer(stu,data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response ({'msg':'data complete  updated'})
        return Response (deserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self ,request,pk=None, format = None):
       
        stu = Student.objects.get(id =pk)
        deserializer = StudentSerializer(stu,data=request.data,partial = True)
        if deserializer.is_valid():
            deserializer.save()
            return Response({'msg':'data partialy updated'})
        return Response(deserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,foemat = None):
       
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response ({'msg':'data deleted'})
        
        
                        
        
from django.shortcuts import render
from rest_framework.views import APIView
from . models import Student
from .serializer import StundentSerializer
from rest_framework.routers import Response
from rest_framework import status


# Create your views here.
class StudentApiView(APIView):
    def get(self,request,pk=None,format =None):
        try:
            id = pk
            print('****************_________++++++++++++++++++++++++')
            if id is not None:
                print(id)
                stu = Student.objects.get(id = id)
                serialzer = StundentSerializer(stu)
                return Response (serialzer.data,status=status.HTTP_200_OK)
            stu = Student.objects.all()
            serialzer = StundentSerializer(stu,many= True)
            return Response(serialzer.data,)
        except Student.DoesNotExist:
            return Response({'msg':'not found'},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,format =None ):
        try:
            deserilizer = StundentSerializer(data=request.data)
            if deserilizer.is_valid():
                deserilizer.save()
                return Response({'msg':'data createed'},status=status.HTTP_201_CREATED)
            return Response ({'msg':'invalid data'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
             return Response({'msg': 'An error occurred while creating the student'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
    def put(self,request,pk =None,format = None):
        stu = Student.objects.get(id =pk)
        deseriliser = StundentSerializer(stu,data=request.data)
        if deseriliser.is_valid():
            deseriliser.save()
            return Response(deseriliser.data,status=status.HTTP_202_ACCEPTED)
        return Response({'msg':'invalid update'})   
    
    def patch(self, request, pk=None, format=None):
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StundentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'msg': 'Invalid update'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(id =pk)
            stu.delete()
            return Response ( ({'msg':'data deleted'}))
        return Response ({'msg':'somthing wrong'})
   
    
              
            
        
      
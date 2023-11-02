from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import Singer , Song
from .serializer import SingerSerilizer , SongSerilizer

class SingerViewset( ModelViewSet):
        queryset = Singer.objects.all()
        serializer_class = SingerSerilizer
        
class Songviewset(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerilizer        
        

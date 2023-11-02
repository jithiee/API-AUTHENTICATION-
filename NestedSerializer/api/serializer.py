from rest_framework import serializers
from . models import Singer , Song


        
class SongSerilizer(serializers.ModelSerializer):
   
    class Meta:
        model = Song
        fields = ['id','title','singer','duration'] 
               

class SingerSerilizer(serializers.ModelSerializer):
    sungby = SongSerilizer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'sungby'] 
        
   
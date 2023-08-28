from rest_framework import serializers
from .models import News, ImgFiles, GameDiscipline

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgFiles
        fields = ['file','name'] 

class NewsSerializers(serializers.ModelSerializer):
    img = ImgSerializer(read_only=True)
    class Meta:
        model = News
        fields = ['id','date','short_text','slug','img']


class GameDisciplineSerializer(serializers.ModelSerializer):
    img = ImgSerializer(read_only=True)
    class Meta:
        model = GameDiscipline
        fields = ["id","name","slug",'img']
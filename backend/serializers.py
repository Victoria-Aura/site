from rest_framework import serializers
from .models import News, ImgFiles

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgFiles
        fields = ['file','name'] 

class NewsSerializers(serializers.ModelSerializer):
    img = ImgSerializer( read_only=True)
    class Meta:
        model = News
        fields = ['id','short_text','slug','img']


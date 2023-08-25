from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import NewsSerializers,ImgSerializer
from .models import News,ImgFiles


@api_view(['GET', 'POST'])
def news_list(request):
    if request.method == 'GET':
        data = News.objects.only('id','short_text','slug','img').select_related('img').all()
        serializer = NewsSerializers(data, context={'request': request}, many=True)
        return Response(serializer.data) 
@api_view(['GET'])
def main_img(request):
    data = ImgFiles.objects.filter(type_img='MN').only('file','name')
    serializer = ImgSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)

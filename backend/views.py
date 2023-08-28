from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework.viewsets import ModelViewSet


from .serializers import NewsSerializers,ImgSerializer,GameDisciplineSerializer
from .models import News,ImgFiles,GameDiscipline


@api_view(['GET'])
def news_list(request):
    if request.method == 'GET':
        data = News.objects.only('id','short_text','slug','img').select_related('img').order_by('-date','-time').all()
        serializer = NewsSerializers(data, context={'request': request}, many=True)
        return Response(serializer.data) 

class GameDisciplineViewSet(ModelViewSet):
    queryset = GameDiscipline.objects.all()
    serializer_class = GameDisciplineSerializer
class ImgViewSet(ModelViewSet):
    queryset = ImgFiles.objects.only('file','name')
    serializer_class = ImgSerializer
    @action(methods=['get'],detail=False)
    def main(self,request):
        data = self.get_queryset().filter(type_img='MN')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
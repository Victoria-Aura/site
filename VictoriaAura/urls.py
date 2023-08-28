from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from backend.views import news_list,  ImgViewSet,GameDisciplineViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'img', ImgViewSet)
router.register('game-discipline',GameDisciplineViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/',news_list),
    path('api/', include(router.urls)),

    # path('api/img/main/',main_img)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

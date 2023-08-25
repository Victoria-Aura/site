from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from backend.views import news_list, main_img

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/',news_list),
    path('api/img/main/',main_img)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

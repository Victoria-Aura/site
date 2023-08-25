from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("short_text", ),"name":("short_text",)}
class ImgAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name':('file',)}
admin.site.register(Countries)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(GameDiscipline)
admin.site.register(Tournament)
admin.site.register(News,NewsAdmin)
admin.site.register(Match)
admin.site.register(ImgFiles,ImgAdmin)
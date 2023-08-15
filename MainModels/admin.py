from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Countries)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(GameDiscipline)
admin.site.register(Match)
admin.site.register(Tournament)

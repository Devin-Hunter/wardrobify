from django.contrib import admin
from .models import Hat, LocationVO

@admin.register(Hat)
class HatAdmin(admin.ModelAdmin):
    pass

@admin.register(LocationVO)
class LocationVoAdmin(admin.ModelAdmin):
    pass
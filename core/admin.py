from django.contrib import admin
from .models import Resource

# Register your models here.
class ResourceAdmin(admin.ModelAdmin):
    list_display  = ('name', 'size', 'content_type', 'storage', 'create_at')
admin.site.register(Resource, ResourceAdmin)
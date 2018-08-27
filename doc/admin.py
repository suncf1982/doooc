from django.contrib import admin
from .models import Doc

# Register your models here.
class DocAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author', 'tech_stack', 'published', 'create_at', 'update_at')
admin.site.register(Doc, DocAdmin)
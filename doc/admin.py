from django.contrib import admin
from .models import Doc, PopularKeyword

# Register your models here.
class DocAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author', 'tech_stack', 'published', 'create_at', 'update_at')
admin.site.register(Doc, DocAdmin)

class PopularKeywordAdmin(admin.ModelAdmin):
    list_display  = ('keyword', 'count', 'update_at')
admin.site.register(PopularKeyword, PopularKeywordAdmin)
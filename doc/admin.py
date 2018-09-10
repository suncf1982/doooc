from django.contrib import admin
from .models import Doc, PopularKeyword, DocTemplate, Favorite, Archive

# Register your models here.
class DocAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author', 'tech_stack', 'published', 'create_at', 'update_at')
admin.site.register(Doc, DocAdmin)

class PopularKeywordAdmin(admin.ModelAdmin):
    list_display  = ('keyword', 'count', 'update_at')
admin.site.register(PopularKeyword, PopularKeywordAdmin)

class DocTemplateAdmin(admin.ModelAdmin):
    list_display  = ('name', 'usage_times', 'create_at', 'update_at')
admin.site.register(DocTemplate, DocTemplateAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display  = ('doc', 'user', 'create_at')
admin.site.register(Favorite, FavoriteAdmin)

class ArchiveAdmin(admin.ModelAdmin):
    list_display  = ('name', 'owner_first_name', 'create_at')

    def owner_first_name(self, obj):
        return obj.owner.first_name
    owner_first_name.short_description = "拥有者"
admin.site.register(Archive, ArchiveAdmin)
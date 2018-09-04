from .models import Doc, PopularKeyword, DocTemplate, Favorite
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from core.serializers import UserReadonlySerializer
from .enums import all_enums


class DocSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    class Meta:
        model = Doc
        fields = '__all__'


class DocReadonlySerializer(TaggitSerializer, serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.first_name')
    tech_stack_name = serializers.CharField(source='get_tech_stack_display', read_only=True)
    tags = TagListSerializerField()
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    class Meta:
        model = Doc
        fields = '__all__'

class UserKVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ('id', 'title')

class PopularKeywordSerializer(serializers.ModelSerializer):
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    class Meta:
        model = PopularKeyword
        fields = '__all__'

class DocTemplateSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    class Meta:
        model = DocTemplate
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteReadonlySerializer(serializers.ModelSerializer):
    doc = DocReadonlySerializer(read_only=True)
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    class Meta:
        model = Favorite
        fields = '__all__'


    
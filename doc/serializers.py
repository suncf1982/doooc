from .models import Doc
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .enums import all_enums


class DocSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    class Meta:
        model = Doc
        fields = '__all__'


class DocReadonlySerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.first_name')
    tech_stack_name = serializers.CharField(source='get_tech_stack_display', read_only=True)
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)
    class Meta:
        model = Doc
        fields = '__all__'

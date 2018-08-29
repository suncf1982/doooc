from rest_framework.decorators import api_view
from django.db.models import Count
from rest_framework import serializers
from rest_framework.response import Response
from taggit.models import TaggedItem

class PopularTagsSerializer(serializers.Serializer):
    tag__name = serializers.CharField(max_length=50)
    count = serializers.IntegerField()

@api_view(['get'])
def popular_tags(request):
    queryset = TaggedItem.objects.values('tag__name').annotate(count=Count('tag__name')).order_by('-count')[:20]
    serializer = PopularTagsSerializer(queryset, many=True)
    return Response(serializer.data)
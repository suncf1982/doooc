from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import PopularKeyword
from ..serializers import PopularKeywordSerializer


@api_view(['get'])
def popular_keywords(request):
    queryset = PopularKeyword.objects.all().order_by('-count')[:20]
    serializer = PopularKeywordSerializer(queryset, many=True)
    return Response(serializer.data)
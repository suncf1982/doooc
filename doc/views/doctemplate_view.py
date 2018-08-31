from ..models import DocTemplate
from ..serializers import DocTemplateSerializer

from django.http import JsonResponse

from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import api_view
import os
from datetime import datetime
import time
from doooc import settings


class DocTemplateList(generics.ListAPIView):
    queryset = DocTemplate.objects.all()
    serializer_class = DocTemplateSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = DocTemplate.objects.all()
        search_word = self.request.query_params.get('search_word', None)

        if search_word is not None and search_word:
            DocTemplate.objects.addKeyword(search_word)
            queryset = queryset.filter(content__contains=search_word)
        return queryset


@api_view(['get'])
def get_template(request, pk):
    obj = DocTemplate.objects.get(pk=pk)
    obj.usage_times = obj.usage_times + 1
    obj.save()
    file_path = obj.storage.path
    with open(os.path.join(settings.BASE_DIR, file_path), 'r', encoding="utf8") as f:
        template_str = f.read()
    context = {
        'content': template_str,
        'template': DocTemplateSerializer(obj).data
    }
    return JsonResponse(context)

from ..models import Doc
from ..serializers import DocSerializer, DocReadonlySerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q
from django.db.models import Count
from rest_framework import serializers
from django.http import HttpResponse, StreamingHttpResponse
import os
import datetime
import time
from doooc import settings


class DocList(generics.ListCreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocReadonlySerializer

    def post(self, request, *args, **kwargs):
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Doc.objects.all()
        search_word = self.request.query_params.get('search_word', None)

        if search_word is not None and search_word:
            queryset = queryset.filter(
                Q(title__contains=search_word) | Q(content__contains=search_word))
        return queryset


class DocDetail(APIView):
    def get_object(self, pk):
        try:
            return Doc.objects.get(pk=pk)
        except Doc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = DocReadonlySerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = DocSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['put'])
def publish(request, pk):
    try:
        obj = Doc.objects.get(pk=pk)
        obj.published = True
        obj.save()
    except Doc.DoesNotExist:
        raise Http404

    return Response(status=status.HTTP_204_NO_CONTENT)


def download_html(request, pk):
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    output = pypandoc.convert(obj.content, 'html', format='md', extra_args=[
                              '--base-header-level=2'])
    response = HttpResponse(output)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s%s"' % (time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())), ".html")
    return response

def download_pdf(request, pk):
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    pypandoc.convert(obj.content, 'pdf', format='md', outputfile=os.path.join(settings.BASE_DIR, 'temp/temp.pdf'), extra_args=['--pdf-engine=xelatex', '-V', 'geometry:margin=1.5cm'])
    with open(os.path.join(settings.BASE_DIR, 'temp/temp.pdf'),'rb') as f:
        c = f.read()
    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s%s"' % (time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())), ".pdf")
    return response

def download_docx(request, pk):
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    pypandoc.convert(obj.content, 'docx', format='md', outputfile=os.path.join(settings.BASE_DIR, 'temp/temp.docx'))
    with open(os.path.join(settings.BASE_DIR, 'temp/temp.docx'),'rb') as f:
        c = f.read()
    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s%s"' % (time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())), ".docx")
    return response

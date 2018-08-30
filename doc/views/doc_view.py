from ..models import Doc, PopularKeyword
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
from datetime import datetime
import time
from doooc import settings

FILE_CACHE_DIR = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'filecache')


class DocList(generics.ListCreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocReadonlySerializer

    def post(self, request, *args, **kwargs):
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        search_word = self.request.query_params.get('search_word', None)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for s in serializer.data:
                content = s['content']
                if search_word is not None:
                    idx = content.find(search_word)
                    start_idx = 0 if idx < 80 else idx-80
                    end_idx = 160 if idx < 80 else idx+80
                    s['searched'] = content[start_idx:end_idx].replace(
                        search_word, '<span style="color: red;margin:0 5px;font-size:16px;">'+search_word+'</span>')
                else:
                    s['searched'] = content[0:160]
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Doc.objects.all()
        search_word = self.request.query_params.get('search_word', None)
        author = self.request.query_params.get('author', '')
        tech_stack = self.request.query_params.get('tech_stack', '')
        tag = self.request.query_params.get('tag', '')

        if search_word is not None and search_word:
            PopularKeyword.objects.addKeyword(search_word)
            queryset = queryset.filter(
                Q(title__contains=search_word) | Q(content__contains=search_word))
        if author != '':
            queryset = queryset.filter(author__id=author)
        if tech_stack != '':
            queryset = queryset.filter(tech_stack=tech_stack)
        if tag != '':
            queryset = queryset.filter(tags__name__in=[tag])

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


def download_md(request, pk):
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    response = HttpResponse(obj.content)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s%s"' % (
        time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())), ".md")
    return response


def download_html(request, pk):
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    output_file_name = obj.update_at.strftime("%Y%m%d%H%M%S%f") + '.html'
    if not os.path.exists(os.path.join(FILE_CACHE_DIR, output_file_name)):
        output = pypandoc.convert(obj.content, 'html', format='md', extra_args=[
                                '--base-header-level=2'])
        with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'w', encoding='utf8') as f:
            f.write(output)
    with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'r', encoding='utf8') as f:
        c = f.read()
    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % (output_file_name, )
    return response


def download_pdf(request, pk):
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    output_file_name = obj.update_at.strftime("%Y%m%d%H%M%S%f") + '.pdf'
    if not os.path.exists(os.path.join(FILE_CACHE_DIR, output_file_name)):
        pypandoc.convert(obj.content, 'pdf', format='md', outputfile=os.path.join(
            FILE_CACHE_DIR, output_file_name), extra_args=['--pdf-engine=pdflatex', '-V', 'geometry:margin=1.5cm', '-V', 'mainfont="SimSun"'])
    with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'rb') as f:
        c = f.read()

    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % (
        output_file_name,)
    return response


def download_docx(request, pk):
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    output_file_name = obj.update_at.strftime("%Y%m%d%H%M%S%f") + '.docx'
    if not os.path.exists(os.path.join(FILE_CACHE_DIR, output_file_name)):
        pypandoc.convert(obj.content, 'docx', format='md', outputfile=os.path.join(
            FILE_CACHE_DIR, output_file_name))
    with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'rb') as f:
        c = f.read()
    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % (
        output_file_name,)
    return response

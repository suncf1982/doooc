'''
文档管理
'''

import os
import time
from datetime import datetime
from django.http import Http404, HttpResponse
from django.db.models import Q
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from doooc import settings
from ..models import Doc, PopularKeyword
from ..serializers import DocSerializer, DocReadonlySerializer, UserKVSerializer

FILE_CACHE_DIR = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'filecache')


class DocList(generics.ListCreateAPIView):
    '''
    列表、新增
    '''
    queryset = Doc.objects.all()
    serializer_class = DocReadonlySerializer

    def post(self, request, *args, **kwargs):
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, update_at=datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        usergroups = list(request.user.groups.values_list('name', flat=True))
        print(usergroups)
        queryset = self.filter_queryset(self.get_queryset())
        if 'admin' not in usergroups:
            queryset = queryset.filter(author=request.user)
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
        tech_stack = self.request.query_params.get('tech_stack', '')
        tag = self.request.query_params.get('tag', '')
        archive = self.request.query_params.get('archive', '')
        if search_word is not None and search_word:
            PopularKeyword.objects.addKeyword(search_word)
            queryset = queryset.filter(
                Q(title__contains=search_word) | Q(content__contains=search_word))
        if tech_stack != '':
            queryset = queryset.filter(tech_stack=tech_stack)
        if tag != '':
            queryset = queryset.filter(tags__name__in=[tag])
        if archive != '':
            queryset = queryset.filter(archive__id=archive)

        return queryset

class SearchList(generics.ListAPIView):
    '''
    搜索
    '''
    queryset = Doc.objects.all()
    serializer_class = DocReadonlySerializer

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
        archive = self.request.query_params.get('archive', '')
        queryset = queryset.filter(published=True)
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
        if archive != '':
            queryset = queryset.filter(archive__id=archive)

        return queryset


class DocDetail(APIView):
    '''
    获取、更新、删除
    '''
    
    # TODO: 主要是为了把get的权限放开，目前的做法put和delete的权限也放开了，需改进
    authentication_classes = (())
    permission_classes = (())

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
            serializer.save(update_at=datetime.now())
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


@authentication_classes(())
@permission_classes(())
def download_md(request, pk):
    '''
    下载md格式文件
    '''
    obj = Doc.objects.get(pk=pk)
    obj.download_times = obj.download_times + 1
    obj.save()
    response = HttpResponse(obj.content)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s%s"' % (
        time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())), ".md")
    return response


@authentication_classes(())
@permission_classes(())
def download_html(request, pk):
    '''
    下载html格式文件
    '''
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    obj.download_times = obj.download_times + 1
    obj.save()
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
    response['Content-Disposition'] = 'attachment;filename="%s"' % (
        output_file_name, )
    return response


@authentication_classes(())
@permission_classes(())
def download_pdf(request, pk):
    '''
    下载pdf格式文件
    '''
    import pypandoc
    obj = Doc.objects.get(pk=pk)
    obj.download_times = obj.download_times + 1
    obj.save()
    output_file_name = obj.update_at.strftime("%Y%m%d%H%M%S%f") + '.pdf'
    if not os.path.exists(os.path.join(FILE_CACHE_DIR, output_file_name)):
        pypandoc.convert(obj.content, 'pdf', format='md', outputfile=os.path.join(
            FILE_CACHE_DIR, output_file_name), extra_args=['--pdf-engine=xelatex', '-V', 'geometry:margin=1.5cm', '-V', 'mainfont="SimSun"'])
    with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'rb') as f:
        c = f.read()

    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % (
        output_file_name,)
    return response


@authentication_classes(())
@permission_classes(())
def download_docx(request, pk):
    '''
    下载word格式文件
    '''
    response = download(pk, 'docx')
    return response


@authentication_classes(())
@permission_classes(())
def download_pptx(request, pk):
    '''
    下载ppt格式文件
    '''
    response = download(pk, 'pptx')
    return response


def download(pk, output_type):
    obj = Doc.objects.get(pk=pk)
    obj.download_times = obj.download_times + 1
    obj.save()
    output_file_name = obj.update_at.strftime(
        "%Y%m%d%H%M%S%f") + '.' + output_type
    if not os.path.exists(os.path.join(FILE_CACHE_DIR, output_file_name)):
        import pypandoc
        pypandoc.convert(obj.content, output_type, format='md', outputfile=os.path.join(
            FILE_CACHE_DIR, output_file_name))
    with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'rb') as f:
        c = f.read()
    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % (
        output_file_name,)

    return response

@authentication_classes(())
@permission_classes(())
def online_ppt(request, pk):
    import pypandoc
    try:
        theme = request.GET['theme']
    except MultiValueDictKeyError:
        theme = 'sky'
    obj = Doc.objects.get(pk=pk)
    output_file_name = '%s_%s%s' % (theme,obj.update_at.strftime("%Y%m%d%H%M%S%f"), '.html')
    if not os.path.exists(os.path.join(FILE_CACHE_DIR, output_file_name)):
        output = pypandoc.convert(obj.content, 'revealjs', format='md', extra_args=['-s','-V','theme=' + theme])
        with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'w', encoding='utf8') as f:
            f.write(output)
    with open(os.path.join(FILE_CACHE_DIR, output_file_name), 'r', encoding='utf8') as f:
        c = f.read()
    response = HttpResponse(c)
    response['Content-Type'] = 'text/html;charset=UTF-8'
    return response

@api_view(['get'])
def popular_docs(request):
    queryset = Doc.objects.values('id', 'title').order_by('-download_times')[:5]
    serializer = UserKVSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['put'])
@authentication_classes(())
@permission_classes(())
def share(request, pk):
    share_to = request.data['share_to']
    try:
        obj = Doc.objects.get(pk=pk)
        url = request.build_absolute_uri('/#/view/' + str(obj.id))
        # send_mail(
        #     '来自于xxx平台的共享文档',
        #     obj.title,
        #     settings.EMAIL_HOST_USER,
        #     [share_to],
        #     fail_silently=False,
        # )
        subject = obj.title
        text_content = ''
        html_content = '<p>有人给您分享了一篇文档： <a href="'+ url +'">'+ url +'</a></p>'
        html_content += '<br /><br />本邮件是由 <a href="'+ request.build_absolute_uri('/') +'">DOOOC</a> 平台发出'
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [share_to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Doc.DoesNotExist:
        raise Http404

    return Response(status=status.HTTP_204_NO_CONTENT)

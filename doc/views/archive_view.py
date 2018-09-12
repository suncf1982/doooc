from ..models import Archive, Doc
from ..serializers import ArchiveSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

class ArchiveList(generics.ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer

    def post(self, request, *args, **kwargs):
        serializer = ArchiveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Archive.objects.filter(owner=self.request.user)
        return queryset

class ArchiveDetail(APIView):
    def get_object(self, pk):
        try:
            return Archive.objects.get(pk=pk)
        except Archive.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        obj = self.get_object(pk)
        serializer = ArchiveSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = ArchiveSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['post','delete'])
def remove_doc(request, archive_id, doc_id):
    try:
        archive = Archive.objects.get(pk=archive_id)
        doc = Doc.objects.get(pk=doc_id)
        if request.method == 'POST':
            archive.docs.add(doc)
        elif request.method == 'DELETE':
            archive.docs.remove(doc)

    except Archive.DoesNotExist:
        raise Http404
    except Doc.DoesNotExist:
        raise Http404

    return Response(status=status.HTTP_204_NO_CONTENT)

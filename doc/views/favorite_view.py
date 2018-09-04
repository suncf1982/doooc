from ..models import Favorite
from ..serializers import FavoriteSerializer, FavoriteReadonlySerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class FavoriteList(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteReadonlySerializer

    def post(self, request, *args, **kwargs):
        serializer = FavoriteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user)
        return queryset

class FavoriteDetail(APIView):
    def get_object(self, pk):
        try:
            return Favorite.objects.get(pk=pk)
        except Favorite.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        obj = self.get_object(pk)
        serializer = FavoriteSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

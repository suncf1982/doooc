from django.contrib.auth.models import User
from core.serializers import UserSerializer, UserReadonlySerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination


@api_view(['GET'])
def user_info(request):
    serializer = UserReadonlySerializer(request.user)
    return Response(serializer.data)

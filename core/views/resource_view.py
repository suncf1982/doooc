from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from django.http import JsonResponse
from core.models import Resource

@api_view(['post'])
@authentication_classes(())
@permission_classes(())
def upload(request):
  file = request.FILES['file']
  instance = Resource()
  instance.name = file.name
  instance.size = file.size
  instance.content_type = file.content_type
  instance.storage = file
  instance.save()

  return JsonResponse({'url': instance.storage.url})

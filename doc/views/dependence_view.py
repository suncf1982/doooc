from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from doc.enums import all_enums


@api_view(['GET'])
def dependences(request):
    """
    枚举-管理端接口

    {
      'enums': ...,
      'regions': ...,
      'inspectors': ...,
      'companies': ...,
      'groups': ...,
      'offices': ...
    }     
    """
    context = {
        'enums': all_enums,
    }
    return JsonResponse(context)

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UserSerializer
import datetime

'''
参考：
http://www.django-rest-framework.org/api-guide/authentication/
If you need a customized version of the obtain_auth_token view, 
you can do so by overriding the ObtainAuthToken view class, 
and using that in your url conf instead.

authtoken认证时，返回token以及用户信息
'''
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        user.last_login = datetime.datetime.now()
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        serializer = UserSerializer(user)
        user = serializer.data
        user['token'] = token.key

        return Response(user)


obtain_auth_token = ObtainAuthToken.as_view()

def jwt_response_payload_handler(token, user=None, request=None):

    serializer = UserSerializer(user)
    user = serializer.data
    user['token'] = token

    return user

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import user_view

urlpatterns = [
    url(r'^user/info/$', user_view.user_info),
]

urlpatterns = format_suffix_patterns(urlpatterns)
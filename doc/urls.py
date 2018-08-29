from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import dependence_view, doc_view, tag_view, keyword_view

urlpatterns = [
    url(r'^dependences/$', dependence_view.dependences),

    url(r'^docs/$', doc_view.DocList.as_view()),
    url(r'^docs/(?P<pk>[0-9]+)/$', doc_view.DocDetail.as_view()),
    url(r'^docs/publish/(?P<pk>[0-9]+)/$', doc_view.publish),
    url(r'^docs/download/md/(?P<pk>[0-9]+)/$', doc_view.download_md),
    url(r'^docs/download/html/(?P<pk>[0-9]+)/$', doc_view.download_html),
    url(r'^docs/download/pdf/(?P<pk>[0-9]+)/$', doc_view.download_pdf),
    url(r'^docs/download/docx/(?P<pk>[0-9]+)/$', doc_view.download_docx),
    url(r'^docs/pupulartags/$', tag_view.popular_tags),
    url(r'^docs/pupularkeywords/$', keyword_view.popular_keywords),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import dependence_view, doc_view, tag_view, keyword_view, doctemplate_view, favorite_view

urlpatterns = [
    url(r'^dependences/$', dependence_view.dependences),

    url(r'^docs/$', doc_view.DocList.as_view()),
    url(r'^docs/(?P<pk>[0-9]+)/$', doc_view.DocDetail.as_view()),
    url(r'^docs/search/$', doc_view.SearchList.as_view()),
    url(r'^docs/publish/(?P<pk>[0-9]+)/$', doc_view.publish),
    url(r'^docs/share/(?P<pk>[0-9]+)/$', doc_view.share),
    url(r'^docs/download/md/(?P<pk>[0-9]+)/$', doc_view.download_md),
    url(r'^docs/download/html/(?P<pk>[0-9]+)/$', doc_view.download_html),
    url(r'^docs/download/pdf/(?P<pk>[0-9]+)/$', doc_view.download_pdf),
    url(r'^docs/download/docx/(?P<pk>[0-9]+)/$', doc_view.download_docx),
    url(r'^docs/download/pptx/(?P<pk>[0-9]+)/$', doc_view.download_pptx),
    url(r'^docs/populardocs/$', doc_view.popular_docs),
    url(r'^docs/pupulartags/$', tag_view.popular_tags),
    url(r'^docs/pupularkeywords/$', keyword_view.popular_keywords),
    url(r'^docs/templates/$', doctemplate_view.DocTemplateList.as_view()),
    url(r'^docs/templates/(?P<pk>[0-9]+)/$', doctemplate_view.get_template),
    url(r'^docs/favorites/$', favorite_view.FavoriteList.as_view()),
    url(r'^docs/favorites/(?P<pk>[0-9]+)/$', favorite_view.FavoriteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
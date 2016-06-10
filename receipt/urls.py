from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^receipt/$', views.ReceiptList.as_view()),
    url(r'^receipt/(?P<pk>[0-9]+)/$', views.ReceiptDetail.as_view()),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import url
from authen import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^add_group/(?P<pk>[0-9]+)/$', views.add_group),
    url(r'^user/$', views.user_list),
    url(r'^add_owner/$', views.add_owner),
    url(r'^auth/$', views.example_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'), # /
    url(r'^post/$', PostLV.as_view(), name='post_list'), # /post/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'), # /post/example/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'), # /archive/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'), # /2012/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'), # /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'), # /2012/nov/10/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'), # /today/
    url(r'^tag/$',TagTV.as_view(), name='tag_cloud'), #/tag/
    url(r'^tag/(?P<tag>[^/]+(?u))/$',PostTOL.as_view(), name='tagged_object_list'), #/tag/tagname/
    url(r'^search/$',SearchFormView.as_view(),name='search'),
]

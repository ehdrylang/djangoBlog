"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static # 정적 파일 처리하는 뷰를 호출하도록 그에맞는 URL패턴을 반환하는 함수
from django.conf import settings # settings.py모듈에서 정의한 항목을 담은 객체를 참조하는 레퍼런스 변수

from blog.views import HomeView
from blog.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/register/$',UserCreateView.as_view(),name='register'),
    url(r'^accounts/register/done/$',UserCreateDoneTV.as_view(),name='register_done'),

    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^photo/',include('photo.urls',namespace='photo')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

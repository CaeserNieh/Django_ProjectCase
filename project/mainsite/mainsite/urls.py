"""mainsite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from mysite.views import homepage,latestnews
from contact import views as contact_views
from django.conf.urls import include
from posts import views as posts_views 

from training import views as train_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',homepage,name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/',contact_views.contact,name='contact'),
    url(r'^latestnews/$',latestnews,name='latestnews'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^posts/$',posts_views.home,name='home'),
    url(r'^posts/(.+)/$',posts_views.news,name='news'),
    url(r'^train/boss/',train_views.trainingboss,name='train_boss'),
    url(r'^train/dealer/',train_views.trainingdealer,name='train_dealer'),


]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
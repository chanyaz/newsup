"""Django18project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^TopN/$', TopN),
    url(r'^insertLanguageCategory/$', insertLanguageCategory),
    url(r'^home/', loadNewsForHome,name="loadNewsForHome"),
    url(r'^cat/', loadNewsForCategory,name="loadNewsForCategory"),
    url(r'^similar/', loadSimilarNews,name="loadSimilarNews"),
    url(r'^loadTopN/', loadTopN,name="loadTopN"),
    url(r'^loadTopNVideo/', loadTopNVideo,name="loadTopNVideo"),
    url(r'^insertVideoLanguageCategory/$', insertVideoLanguageCategory),
    url(r'^videoCat/', loadVideoForCategory,name="loadVideoForCategory"),
    url(r'^isVideoAvailable/', isVideoAvailable,name="isVideoAvailable"),
    url(r'^catNew/', loadNewsForCategoryNew,name="loadNewsForCategoryNew"),
    url(r'^similarNew/', loadSimilarNewsNew,name="loadSimilarNewsNew"),
    url(r'^sourceNews/', sourceNews,name="sourceNews"),
    url(r'^socialIndicator/$', socialIndicator),

]

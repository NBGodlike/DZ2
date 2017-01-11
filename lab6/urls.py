"""lab6 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
 https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
 1. Add an import: from my_app import views
 2. Add a URL to urlpatterns: url(r'^$', views.home, name='home')
Class-based views
 1. Add an import: from other_app.views import Home
 2. Add a URL to urlpatterns: url(r'^$', Home.as_view(), name='home')
Including another URLconf
 1. Import the include() function: from django.conf.urls import url,
include
 2. Add a URL to urlpatterns: url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from users.views import index,registration,login,Logout,Online,PostView,createcourse,sub,CourseListView
urlpatterns = [
 url(r'^admin/', admin.site.urls),
 url(r'^$', index),
 url(r'^login/$', login),
 url(r'^registration/$', registration),
 url(r'^logout/$', Logout.as_view()),
 url(r'^course/$', Online.as_view()),
 url(r'^course/(?P<pk>\d+)/$', PostView.as_view(), name="Course"),
 url(r'^course_list/(?P<page>\d+)/$', CourseListView.as_view()),
 url(r'^sub/$', sub),
 url(r'^create/$', createcourse),
]

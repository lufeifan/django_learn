
from django.contrib import admin
from django.urls import path,include,re_path
from . import view              #导入view.py
from blog import views
from django.views.static import serve
#导入静态文件模块
from django.conf import settings
#导入配置文件里的文件上传配置 
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', view.index),       #使用view.py里的hello方法
    # path('ueditor/', include('DjangoUeditor.urls')), #添加DjangoUeditor的URL
    # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行

    path('admin/', admin.site.urls),#管理后台
    path('', views.index, name='index'),#网站首页
    path('list-<int:lid>.html', views.list, name='list'),#列表页
    path('show-<int:sid>.html', views.show, name='show'),#内容页
    path('tag/<tag>', views.tag, name='tags'),#标签列表页
    path('s/', views.search, name='search'),#搜索列表页
    path('about/', views.about, name='about'),#联系我们单页
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

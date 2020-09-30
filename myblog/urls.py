"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve  # 富文本,  导入静态文件模块
from django.conf import settings  # 导入配置文件中文件上传配置
# 富文本编辑器中上传图片不显示，添加 re_path
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),  # 管理后台
    path('', views.index, name='index'), #网站首页
    path('list-<int:lid>.html', views.list, name='list'),#列表页
    path('show-<int:sid>.html', views.show, name='show'),#内容页
    path('tag/<tag>',views.tag, name='tags'),#标签搜索页
    path('s/', views.search, name='search'), #搜索列表页
    path('about/',views.about, name='about'), #联系我们
    path('blog/', include('blog.urls', namespace='blog')),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('comment/', include('comment.urls', namespace='comment')),
    # 添加Django的URL
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 富文本图片显示相关

]

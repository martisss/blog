



from django.urls import path
from blog import views, admin

app_name = 'blog'

urlpatterns = [


    # path('', views.index, name='index'),  # 网站首页
    # path('list-<int:lid>.html', views.list, name='list'),  # 列表页
    path('show-<int:sid>.html', views.show, name='show'),  # 内容页
    # path('tag/<tag>', views.tag, name='tags'),  # 标签搜索页
    # path('s/', views.search, name='search'),  # 搜索列表页
    # path('about/', views.about, name='about'),  # 联系我们

]
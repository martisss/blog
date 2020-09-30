from django.contrib import admin
from blog.models import Banner, Category, Tag, Tui, Article, Link

admin.site.site_header = '博客管理后台'
admin.site.site_title = '我的博客'
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'title', 'tui', 'user', 'views', 'created_time','modified_time','paixu')
    # 列表想要显示的字段
    list_per_page =  50
    # 满50条数据自动分页
    ordering = ('-created_time',)
    list_display_links =  ('id', 'title')
    actions_on_bottom = True
    search_fields = ['title']
    list_filter = ['user', 'category']
    date_hierarchy = 'created_time'

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id','name','link_url')


def site(request):
    return None
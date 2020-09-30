from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, Banner, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 导入分页插件包
from comment.models import Comment
# Create your views here.

# 首页
def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]  # 查询幻灯片数据，并切片
    tui = Article.objects.filter(tui_id=2)[:5]
    allarticle = Article.objects.all().order_by('-id')[0:10]  # 获取最新的十篇文章
    # hot = Article.objects.all().order_by('?')[:10]#随机推荐
    hot = Article.objects.filter(tui_id=3)[:10]  # 通过推荐进行查询，以推荐ID是3为例
    # hot = Article.objects.all().order_by('views')[:10]  # 通过浏览数进行排序
    remen = Article.objects.filter(tui_id=1)[:2]
    tags = Tag.objects.all()
    link = Link.objects.all()
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'tui': tui,
        'allarticle': allarticle,
        'hot': hot,
        'remen': remen,
        'tags': tags,
        'link': link,

    }
    return render(request, 'index.html', context)


# 列表页
def show(request, sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分类
    tags = Tag.objects.all()  # 右侧所有标签
    comments = Comment.objects.filter(article= sid)
    context = {'article': show,  'comments': comments}
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())


# 内容页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询文章
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)

    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())


# 标签页
def list(request, lid):
    list = Article.objects.filter(category_id=lid)  # 获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)  # 获取当前文章栏目名
    remen = Article.objects.filter(tui_id=1)[:6]  # 右侧热门推荐
    allcategory = Category.objects.all()
    tags = Tag.objects.all()  # y右侧文章所有标签
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'list.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())


# 关于我们

def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())
# def index(request):
#    sitename = '哲学'
#    url = 'www.philosophy.cn'
#    list = [
#        '开发前的准备',
#        '项目需求分析',
#        '数据库设计分析',
#        '创建项目',
#        '基础配置',
#        '欢迎页面',   '欢迎页面',
# region Description
#        '创建数据库模型',
# endregion
#    ]
#    mydict = {
#        'name': 'eric',
#        'qq': '2466632626',
#        'wx': 'dfsadfadf',
#        'email': '2466632626@qq.com',
#        'Q群': '45356463456',
#    }
#    allarticle = Article.objects.all()
#    context  = {
#        'sitename': sitename,
#        'url':url,
#        'list':list,
#        'mydict':mydict,
#        'allarticle': allarticle,
#    }
#    return  render(request, 'index.html',context)

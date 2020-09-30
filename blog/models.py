from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField  # 导入DjangoUeditor之后需增加此行
from django.urls import reverse


# Django自带用户模块

# 文章分类
class Category(models.Model):
    name = models.CharField(verbose_name='博客分类', max_length=100)  # verbose_name修改在后台管理页面的名字
    index = models.IntegerField(default=999, verbose_name='分类排序')

    # ？？？？？？？？？？？？
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐位
class Tui(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联分类表与分类，一对多  models.CASCADE 表示级联删除，删除分类时，下属文章也全部删除
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True, )
    # 使用外键关联标签表和标签，多对多
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    # body = models.TextField()   #导入DjangoUeditor之前 ； blank=True 意味着文章可以没有标签
    # 导入之后
    body = UEditorField('内容', width=800, height=500, toolbars="full",
                        imagePath="upimg/", filePath="upfile/", upload_settings={"imageMaxSize": 120400},
                        settings={}, command=None, blank=True
                        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    # 此User从django.contrib.auth.models导入，通过外键将文章与User联系
    views = models.PositiveIntegerField('阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    def paixu(self):
        return self.category.index

    paixu.short_description = '分类排序'

    def get_absolute_url(self):
        return reverse('blog:show', args=[self.id])

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


# 幻灯片图表
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


# 友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from blog.models import Article
from .forms import CommentForm
from .models import Comment


# Create your views here.
@login_required(login_url='/userprofile/login/')
def post_comment(request, sid):
    article = get_object_or_404(Article, id=sid)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect(article)  # 当其参数是一个Model实例对象时，会自动调用这个Model对象的get_absolute_url()方法；
        #是article而不是Article
        else:
            return HttpResponse('表单内容有误')
    else:
        return HttpResponse('发表评论仅接收POST请求')

# @login_required(login_url='/userprofile/login/')
# # def del_comment(request,sid):
# #     article = get_object_or_404(Article, id=sid)
# #     comment = Comment.objects.get(id=sid)
# #     comment.delete()
# #     comment.save()
# #     return redirect(article)
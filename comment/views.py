from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from article.models import ArticlePost
from .forms import CommentForm


# Create your views here.
# TODO:评论的Markdown语法，表情符号，更新评论，删除评论etc.
# 文章评论
@login_required(login_url='/userprofile/login/')
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    # 处理POST请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            '''redirect的参数是一个Model对象时，
            会自动调用这个Model对象的get_absolute_url()方法'''
            return redirect(article)
        else:
            return HttpResponse('表单内容有误，请重新填写')
    else:
        return HttpResponse('发表评论仅接受POST请求')

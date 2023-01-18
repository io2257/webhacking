from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from main.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'main/index.html')
def blog(request):
    postlist = Post.objects.order_by('-create_date')
    page = request.GET.get('page','1')
    paginator = Paginator(postlist, 10)
    page_obj = paginator.get_page(page)
    # blog.html을 열 때 postlist도 같이 가져온다
    return render(request, 'main/blog.html', { 'postlist' : page_obj})
def posting(request, pk):
    # 게시글(Post) 중 pk를 이용해 하나의 게시글(post)를 검색
    post = get_object_or_404(Post, pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)를 post라는 이름으로 가져옴
    return render(request, 'main/posting.html',{ 'post' : post })
@login_required(login_url='common:login')
def new_post(request):
    if request.method == "POST":
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                author=request.user,
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                create_date= timezone.now(),
            )
        else:
            new_article=Post.objects.create(
                author=request.user,
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto='',
                create_date=timezone.now(),
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')
def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/blog')
    return render(request, 'main/remove_post.html',{'Post' : post})
@login_required
def post_modify(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, 'Permission denied')
        return redirect('main:posting',pk=pk)
    if request.method == "POST":
        post.author=request.user
        post.postname=request.POST['postname']
        post.contents=request.POST['contents']
        post.mainphoto=request.POST['mainphoto']
        post.create_date=timezone.now()
        post.save()
        return redirect('/blog/'+str(pk),{'post' : post})
    return render(request, 'main/new_post.html')
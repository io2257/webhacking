from django.shortcuts import render, redirect
from django.utils import timezone
from main.models import Post
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'main/index.html')
def blog(request):
    postlist = Post.objects.all()
    page = request.GET.get('page','1')
    paginator = Paginator(postlist, 10)
    page_obj = paginator.get_page(page)
    # blog.html을 열 때 postlist도 같이 가져온다
    return render(request, 'main/blog.html', { 'postlist' : page_obj})
def posting(request, pk):
    # 게시글(Post) 중 pk를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)를 post라는 이름으로 가져옴
    return render(request, 'main/posting.html',{ 'post' : post })
def new_post(request):
    if request.method == "POST":
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                create_date= timezone.now(),
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
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
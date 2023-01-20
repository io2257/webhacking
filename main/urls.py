from django.contrib import admin
from django.urls import path,include
from main.views import index, blog, posting, new_post, remove_post, post_modify
# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/',posting,name='posting'),
    path('blog/new_post/', new_post, name='new_post'),
    path('blog/<int:pk>/remove/',remove_post, name='remove_post'),
    path('blog/modify/<int:pk>/', post_modify, name='post_modify'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
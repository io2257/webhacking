from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    postname = models.CharField(max_length=200)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    create_date = models.DateTimeField()
    # postname이 Post object 대신 나오게 함
    def __str__(self):
        return self.postname
from django.db import models

# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=200)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    create_date = models.DateTimeField()
    # postname이 Post object 대신 나오게 함
    def __str__(self):
        return self.postname
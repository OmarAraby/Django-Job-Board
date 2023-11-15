from django.db import models
from django.contrib.auth.models import User
from job.models import Category ,image_upload
# Create your models here.




class Blog(models.Model):
    author = models.ForeignKey(User ,related_name='blog_auther', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    image= models.ImageField(upload_to=image_upload)




    def __str__(self):
        return self.title
    



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} on {self.blog.title}'

    class Meta:
        ordering = ['-published_at']



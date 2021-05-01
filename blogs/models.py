from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])


class Comment(models.Model): 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    text = models.TextField()

    
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text




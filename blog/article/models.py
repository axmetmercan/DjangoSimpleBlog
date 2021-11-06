from typing import Match
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.base import Model

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=50, verbose_name='Title')
    content = RichTextField(verbose_name='Content')
    article_image = models.FileField(blank= True, null= True, verbose_name='Picture')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    # To show title name at articles page.
    def __str__(self):
        return self.title

    class Meta:
            ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name='Essay',related_name='comments')
    comment_author = models.CharField(max_length= 50, verbose_name= 'Name')
    comment_content = models.CharField(max_length=200, verbose_name='Comment')
    comment_date = models.DateTimeField(auto_now_add= True)
        

    def __str__(self):
        return self.comment_content


    class Meta:
        ordering = ['-comment_date']





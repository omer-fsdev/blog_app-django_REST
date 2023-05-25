from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FixFieldModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True   # Means 'Dont need a table for this model. Dont create it.'

class BlogCategory(FixFieldModel):
    name = models.CharField(max_length=30)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class BlogPost(FixFieldModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    viewed = models.IntegerField(verbose_name='Views', default=0, editable=False)
    blog_category = models.ForeignKey(BlogCategory, verbose_name='Category Name', on_delete=models.CASCADE, related_name='blog_category_name')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class BlogComment(FixFieldModel):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    comment = models.TextField(blank=True)
    blog_post = models.ForeignKey(BlogPost, verbose_name='Post Name', on_delete=models.CASCADE, related_name='blog_post_name')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.blog_post}'
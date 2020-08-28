from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name 

class Article(models.Model):
    title = models.CharField(max_length=200)
    picture = models.FileField()
    body = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    lead = models.BooleanField(default=False)
    lead2 = models.BooleanField(default=False)
    lead3 = models.BooleanField(default=False)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('single', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    post_comment = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.post_comment
    

    
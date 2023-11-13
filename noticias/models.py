from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.URLField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fpt.m.wikipedia.org%2Fwiki%2FFicheiro%3AFlag_Blank.svg&psig=AOvVaw1M3X9dn1LhG_izFTfw8zX4&ust=1699909154871000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCIiszp6tv4IDFQAAAAAdAAAAABAQ')
    published_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.created_date}'
    
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    intro = models.TextField(max_length=250)
    body = models.TextField()
    url = models.FileField(null=True, blank=True)
    published = models.BooleanField(default=False)
    published_on = models.DateTimeField(null=True, blank=True, editable=False)
    categories = models.ManyToManyField(Category)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}".format(self.title)




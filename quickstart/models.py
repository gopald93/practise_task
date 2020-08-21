from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
class Book(models.Model):
    name= models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = datetime.datetime.now()
        self.save()

    def __str__(self):
        return self.title

class Bookdata(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title        


class Bookdataone(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 


class Bookdatatwo(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True,blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title                        
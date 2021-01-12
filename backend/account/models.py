from django.db import models
from backend.community.models import Post


class Account(models.Model):
    email = models.EmailField(max_length=128)
    password = models.EmailField(max_length=50)
    pubDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.email) > 20:
            return self.email[0:20] + '...'
        return self.email


class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    phoneNumber = models.TextField(max_length=12)
    username = models.TextField(max_length=20)

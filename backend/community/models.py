from django.db import models
from account.models import Account


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
    pubDate = models.DateTimeField('date published')
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=100)
    pubDate = models.DateTimeField('date published')

    def __str__(self):
        if len(self.body) > 20:
            return self.body[0:20] + '...'
        return self.body

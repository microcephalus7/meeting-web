from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=128)
    password = models.EmailField(max_length=50)
    pubDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.email) > 20:
            return self.email[0:20] + '...'
        return self.email

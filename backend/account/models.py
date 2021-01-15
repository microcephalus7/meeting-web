from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=128)
    password = models.EmailField(max_length=50)
    pubDate = models.DateTimeField(auto_now_add=True, null=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.email) > 20:
            return self.email[0:20] + '...'
        return self.email


class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    pubDate = models.DateTimeField(auto_now_add=True, null=True)
    updateDate = models.DateTimeField(auto_now=True)
    phoneNumber = models.TextField(max_length=12, null=True)
    username = models.TextField(max_length=20, null=True)
    male = models.BooleanField(null=True)
    birthday = models.DateField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def checkProfile(self):
        if None in [self.account, self.phoneNumber, self.username, self.male, self.birthday]:
            return False
        else:
            return True

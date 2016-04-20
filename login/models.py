from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    ccType = models.CharField(max_length=20)
    ccNumber = models.CharField(max_length=16)
    expDate = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=10, default='Silver')
    credits = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

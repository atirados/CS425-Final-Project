from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.CharField(max_length=50)
    def __unicode__(self):
        return self.title

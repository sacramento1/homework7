from django.db import models
from django.contrib.auth.models import User
from django.forms import forms


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.owner.first_name

class Media(models.Model):
    owner = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(default='bek.png')

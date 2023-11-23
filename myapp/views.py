from django.shortcuts import render
from .models import Post, Media

# Create your views here.
def main(request):
    posts = Post.objects.all()
    media = Media.objects.all()
    return render(request, 'main.html', {'posts':posts, 'media': media})

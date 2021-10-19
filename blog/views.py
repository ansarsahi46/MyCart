from django.shortcuts import render
from .models import blogPosts
from django.http import HttpResponse

# Create your views here.
def index (request):
    myposts = blogPosts.objects.all()


    return render(request, 'blog/index.html', {'myposts': myposts})
def blogpost (request, id):
    mypost = blogPosts.objects.filter(post_id = id)[0]

    latest = blogPosts.objects.last()
    return render(request, 'blog/blogpost.html', {'mypost' : mypost, 'latest': latest})


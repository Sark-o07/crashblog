from django.shortcuts import render
from django.http import HttpResponse
from blog.models import PostModel

# Create your views here.

def frontpage(request):
    posts = PostModel.objects.filter(status=PostModel.ACTIVE)
    context = {
        'posts': posts,
    }
    return render(request, 'core/frontpage.html', context)

def aboutpage(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        'User-Agent: *',
        'Disallow: /admin/',
    ]
    return HttpResponse('\n'.join(text), content_type='text/plain')
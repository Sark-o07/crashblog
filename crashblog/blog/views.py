from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm
from .models import PostModel, CategoryModel

# Create your views here.

def detail(request, category_slug, slug):
    post = get_object_or_404(PostModel, slug=slug, status=PostModel.ACTIVE)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post-detail', slug=slug)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)

def category(request, slug):
    category = get_object_or_404(CategoryModel, slug=slug)
    posts = category.posts.filter(status=PostModel.ACTIVE)
    
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')
    
    posts = PostModel.objects.filter(status=PostModel.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})
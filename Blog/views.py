from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from Blog.models import Post

def index(request):
    posts = Post.objects.all().order_by("-created_at")
    pesquisa = request.POST.get('pesquisa')
    if (request.method == "GET"):
        paginator = Paginator(posts, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'frontend/index.html', {'posts': posts})
    else:
        pesquisa = Post.objects.filter(title__icontains = pesquisa)
        return render(request, 'frontend/index.html', {'posts': pesquisa})

def post(request, slug):
    post = get_object_or_404(Post, slug = slug )
    return render(request, 'frontend/post.html', {'post':post})

def registro(request):
    if (request.method == 'GET'):
        return render(request, 'frontend/registro.html')

def teste(request):
    pass
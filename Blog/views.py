from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from Blog.models import Post, Comentario
from django.contrib.auth import login as dj_login, authenticate, logout as dj_logout
from django.contrib.auth.models import User


# Pagina principal --------------------------------------------------------------------------------------------------

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

# Post e comentários ------------------------------------------------------------------------------------------------

def post(request, slug):
    post = get_object_or_404(Post, slug = slug )
    comentarios = Comentario.objects.filter(post_id = post)
    if request.method == 'GET':
        return render(request, 'frontend/post.html', {'post':post, 'comentarios':comentarios})

    else:
        user = request.user
        postid = request.POST.get('postid')
        comentario = request.POST.get('comentario')
        coment = Comentario.objects.create(content = comentario, post_id = postid, user = user)
        coment.save()

        return redirect(f'post/{post.slug}')


# Autenticação ------------------------------------------------------------------------------------------------------

def registro(request):
    if (request.method == 'GET'):
        return render(request, 'frontend/registro.html')
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('repetirpassword')

        user = User.objects.filter(username = username).first()
        user_email = User.objects.filter(email = email).first()

        dados = {
            'username': username,
            'email': email,
            'password': password,
            're_password': re_password
        }

        if user:
            print("usuario ja cadastrado")
            return render(request, 'frontend/registro.html', {'dados': dados})
        elif user_email:
            print('email ja foi utilizado')
            return render(request, 'frontend/registro.html', {'dados': dados})
        elif password != re_password:
            print('as senhas não são iguais')
            return render(request, 'frontend/registro.html', {'dados': dados})
        else:
            user_cadastro = User.objects.create_user(username=username, email=email, password=password)
            user_cadastro.save()
            return redirect('/')

def login(request):
    if request.method == 'GET':
        return render(request, 'frontend/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        dados = {
            'username': username,
            'password': password,
        }

        if user is not None:
            dj_login(request, user)
            return redirect('/')
        else:
            print('usuario ou a senha está incorreto')
            print(dados)
            return render(request, 'frontend/login.html', {'dados': dados})

def logout(request):
    dj_logout(request)
    return redirect('/')
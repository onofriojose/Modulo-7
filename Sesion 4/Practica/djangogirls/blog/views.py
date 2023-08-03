from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Post
from django.utils import timezone

def index(request):
    posts = Post.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
        }
    return HttpResponse(template.render(context, request))

def agregar(request):
    template = loader.get_template('agregar.html')
    return  HttpResponse(template.render({}, request))



def agregarregistro(request):
    if request.method == 'POST':
        titulo = request.POST.get('title')  # Utiliza request.POST.get() en lugar de request.POST()
        contenido = request.POST.get('text')  # Utiliza request.POST.get() en lugar de request.POST()
        autor = request.POST.get('author')  # Utiliza request.POST.get() en lugar de request.POST()
        fecha_publicacion = timezone.now()
        nuevo_post = Post(title=titulo, text=contenido, author=autor, published_date=fecha_publicacion)
        nuevo_post.save()
        return redirect('index')
    else:
        return render(request, 'agregar.html')

def eliminar(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

def actualizar(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('actualizar.html')
    context = {
        'post' : post,
    }
    return HttpResponse(template.render(context, request))

def actualizar(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.author = request.POST.get('author')
        post.published_date = timezone.now()
        post.save()
        return redirect('index')
    else:
        template = loader.get_template('actualizar.html')
        context = {
            'post': post,
        }
        return HttpResponse(template.render(context, request))

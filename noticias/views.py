from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def home(request):
    return render(request, 'noticias/home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'noticias/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'noticias/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        Post.objects.create(
            titulo=request.POST['titulo'],
            conteudo=request.POST['conteudo']
        )
        return redirect('post_list')
    return render(request, 'noticias/post_form.html')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.titulo = request.POST['titulo']
        post.conteudo = request.POST['conteudo']
        post.save()
        return redirect('post_list')
    return render(request, 'noticias/post_form.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'noticias/post_confirm_delete.html', {'post': post})
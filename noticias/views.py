from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def home(request):
    return render(request, 'noticias/home.html')

def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'noticias/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'noticias/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = form.cleaned_data['image']
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'noticias/post_form.html', {'form': form})

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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'noticias/post_edit.html', {'form': form})
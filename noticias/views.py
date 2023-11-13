from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'noticias/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'noticias/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-created_date')
        context['comment_form'] = CommentForm()
        return context

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'noticias/post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'noticias/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'noticias/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

def home(request):
    return render(request, 'noticias/home.html')

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'noticias/comment_form.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

add_comment = CommentCreateView.as_view()

class CategoryListView(ListView):
    model = Category
    template_name = 'noticias/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(ListView):
    model = Post
    template_name = 'noticias/category_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(categories__in=[category])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context

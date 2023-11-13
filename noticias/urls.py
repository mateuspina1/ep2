from django.urls import path
from .views import home, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, add_comment, CategoryDetailView, CategoryListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('', home, name='home'),
    path('<int:pk>/comment/', add_comment, name='add_comment'),
]
from django.urls import path
from .views import home, post_list, post_detail, post_create, post_edit, post_delete, post_new
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .views import home, post_list, post_detail, post_create, post_edit, post_delete

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('new/', post_create, name='post_create'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
]
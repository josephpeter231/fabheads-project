from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

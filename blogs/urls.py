from django.urls import path
from .views import BlogListView , BlogDetailView, BlogUpdateView,  BlogDeleteView, CommentCreateView

urlpatterns = [
    path('blog/<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('', BlogListView.as_view(), name='blog_list'),

   
    
]
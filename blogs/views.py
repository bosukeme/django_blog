from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog, Comment

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'


class BlogDetailView(DetailView): # new
    model = Blog
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class BlogUpdateView(UpdateView): # new
    model = Blog
    fields = ('title', 'body',)
    template_name = 'blog_edit.html'

class BlogDeleteView(DeleteView): # new
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')


class CommentCreateView(CreateView):
    model = Blog
    template_name = "comment.html"
    fields = ['author', 'body']
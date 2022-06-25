from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DetailView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "description"]
    success_url  = 'base.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post 
    fields = ["title", "description"]
    success_url  = 'base.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    fields = ["title", "description"]
    success_url  = '/'
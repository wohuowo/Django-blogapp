#from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Post


class PostCreateView(CreateView):
    #specifying model for create view
    model = Post
    #specifying fields to be displayed
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostListView(ListView):
    #specifying the model for list view
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model= Post
    fields ="__all__"
    success_url = reverse_lazy("blog:all")    

from django.shortcuts import render
from .models import Pepe
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class bloglistview(ListView):
    model = Pepe
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Pepe
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Pepe
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Pepe
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Pepe
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import TemplateView,ListView
from .models import Book,BookForm
from django.urls import reverse_lazy

class show(TemplateView):
    template_name='CRUD/list_posts.html'
    model=Book
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list']=Book.objects.all()
        return context


class edit(UpdateView):
    model=Book
    fields="__all__"
    success_url="/CRUD/"


class add(CreateView):
    model=Book
    fields="__all__"
    success_url="/CRUD/"

class delete(DeleteView):
    model=Book
    success_url=reverse_lazy("show")


from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed
#from cats.forms import MakeForm

# Create your views here.



class CatList(LoginRequiredMixin, View) :
    def get(self, request):
        cc = Cat.objects.all();
        bl = Breed.objects.all();
        bc = Breed.objects.all().count();
        ctx = { 'cat_list': cc, 'breed_list': bl, 'breed_count':bc };
        return render(request, 'cats/cat_list.html', ctx)

class BreedList(LoginRequiredMixin,View) :
    def get(self, request):
        bl = Breed.objects.all();                     # bl stands for breed list
        bc = Breed.objects.all().count();             #bc stands for breed count
        ctx = { 'breed_list': bl, 'breed_count':bc };
        return render(request, 'cats/breed_list.html', ctx)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedCreate(LoginRequiredMixin,CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


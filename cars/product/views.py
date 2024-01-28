from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *


class CategoryView(ListView):
    model = Category
    template_name = 'product_cat.html'
    context_object_name = 'category'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('categoryView')

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'product_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categoryView')

    def form_valid(self, form):
        return super().form_valid(form)


class MarkaView(ListView):
    model = Marka
    template_name = 'product_marka.html'
    context_object_name = 'marka'


class MarkaDeleteView(DeleteView):
    model = Marka
    template_name = 'category_delete.html'
    success_url = reverse_lazy('markaView')

    def form_valid(self, form):
        return super().form_valid(form)


class MarkaCreateView(CreateView):
    model = Marka
    template_name = 'product_form.html'
    form_class = MarkaForm
    success_url = reverse_lazy('markaView')

    def form_valid(self, form):
        return super().form_valid(form)


class CarCreateView(CreateView):
    model = Car
    template_name = 'product_form.html'
    form_class = CarForm
    success_url = reverse_lazy('carView')

    def form_valid(self, form):
        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Car
    template_name = 'product_detail.html'
    context_object_name = 'car'


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'product_form.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy('carDetailView', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super().form_valid(form)


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'product_delete.html'
    success_url = reverse_lazy('carView')

    def form_valid(self, form):
        return super().form_valid(form)


class CarView(ListView):
    model = Car
    template_name = 'product_list.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['marks'] = Marka.objects.all()
        context['years'] = Car.objects.values_list('year', flat=True).distinct()
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        marka = self.request.GET.get('marka')
        year = self.request.GET.get('year')

        queryset = Car.objects.all()

        if category:
            category_object = Category.objects.get(name=category)
            queryset = queryset.filter(category=category_object)

        if marka:
            marka_object = Marka.objects.get(title=marka)
            queryset = queryset.filter(marka=marka_object)

        if year:
            queryset = queryset.filter(year=year)

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'product_form.html'

    def get_success_url(self):
        return reverse_lazy('carDetailView', kwargs={'pk': self.object.car_id})

    def form_valid(self, form):
        form.instance.car_id = self.kwargs['pk']
        return super().form_valid(form)

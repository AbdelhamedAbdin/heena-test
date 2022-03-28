from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from .models import Product
from django.db.models import Q
from .forms import UpdateProduct
from django.urls import reverse_lazy, reverse


class ProductList(ListView):
    model = Product
    template_name = 'myapp/products.html'
    context_object_name = "products"

    def get_queryset(self):
        if 'search' in self.request.GET:
            return Product.objects.filter(
                Q(name__icontains=self.request.GET.get('search')) |
                Q(price__icontains=self.request.GET.get('search'))
            )
        return self.model.objects.all()


class ProductDetails(DetailView):
    model = Product
    pk_url_kwarg = 'pk'
    queryset = Product.objects.all()
    template_name = 'myapp/product_detail.html'
    context_object_name = "product"


class ProductUpdate(UpdateView):
    form_class = UpdateProduct
    pk_url_kwarg = 'pk'
    queryset = Product.objects.all()
    template_name = 'myapp/product_update.html'
    context_object_name = "product"

    def get_success_url(self):
        if 'pk' in self.kwargs:
            return reverse_lazy('myapp:product-update', kwargs={'pk': int(self.kwargs['pk'])})


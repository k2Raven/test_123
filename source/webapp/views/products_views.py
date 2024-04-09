from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from webapp.models import Product, Category
from webapp.forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['category__title', 'title']
    queryset = Product.objects.exclude(qty=0)

    def dispatch(self, request, *args, **kwargs):
        print(request.session.get('cart'))
        return super().dispatch(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_view.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('index')


def category_add_view(request):
    if request.method == "GET":
        return render(request, 'products/category_create.html')
    elif request.method == 'POST':
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return redirect('index')

from django.db.models import Count, Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, CreateView
from django.urls import reverse_lazy
from django.db.models import F

from webapp.models import Product, Cart, OrderProduct
from webapp.forms import OrderForm
from django.contrib import messages


class ProductAddToCartView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['pk'])
        cart = request.session.get('cart', {})
        # {'1': 3, '2': 2, '3': 1}
        if str(product.id) in cart:
            full_qty = cart[str(product.id)] + 1
        else:
            full_qty = 1

        if product.qty >= full_qty:
            cart[str(product.id)] = full_qty
            messages.success(request, f'Продукт "{product.title}" добавили в корзину')
        else:
            messages.error(request, f'error')

        request.session['cart'] = cart
        # carts = Cart.objects.filter(product=product)
        # if carts:
        #     cart = carts.first()
        #     if product.qty > cart.qty:
        #         cart.qty += 1
        #         cart.save()
        # else:
        #     if product.qty > 0:
        #         Cart.objects.create(product=product, qty=1)

        return redirect('index')


class CartsView(TemplateView):
    template_name = 'carts/carts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        carts = []
        total = 0
        for key, qty in cart.items():
            product = get_object_or_404(Product, id=key)
            total += product.price * qty
            carts.append({'product_id': key, 'title': product.title, 'qty': qty, 'total': product.price * qty,
                          'price': product.price})
        context['carts'] = carts
        context['total'] = total
        context['form'] = OrderForm()
        return context


class ProductDeleteOfCartView(View):
    def get(self, request, *args, **kwargs):
        cart = self.request.session.get('cart', {})
        cart.pop(str(kwargs['pk']))
        self.request.session['cart'] = cart
        return redirect('carts_view')


class OrderCreateView(CreateView):
    form_class = OrderForm

    def form_valid(self, form):
        order = form.save()
        cart = Cart.objects.all()
        for cart_item in cart:
            OrderProduct.objects.create(product=cart_item.product, order=order, qty=cart_item.qty)
        cart.delete()
        return redirect('index')

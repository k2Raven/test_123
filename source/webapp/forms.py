from django import forms
from webapp.models import Category, Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'image', 'qty', 'category')

    def clean_title(self):
        title = self.cleaned_data['title']
        title_old = self.initial.get('title')
        if not title_old or title != title_old:
            if Product.objects.filter(title=title).exists():
                raise forms.ValidationError('Продукт с таким названием существует')
        return title


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'address', 'telephone')


from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='products',
                                 verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')
    image = models.URLField(verbose_name='Изображение')
    qty = models.PositiveIntegerField(default=1, verbose_name='Остаток')


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='products',
                                verbose_name='Продукт')
    qty = models.PositiveIntegerField(default=0, verbose_name='Количество')

    @classmethod
    def get_full_total(cls):
        full_total = 0
        for entry_in_cart in cls.objects.all():
            full_total += entry_in_cart.qty * entry_in_cart.product.price
        return full_total


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    telephone = models.CharField(max_length=50, verbose_name='Телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    products = models.ManyToManyField('webapp.Product', related_name='orders', through='webapp.OrderProduct',
                                      through_fields=('order', 'product'), verbose_name='Продукты')


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='product_orders')
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE, related_name='order_products')
    qty = models.PositiveIntegerField(verbose_name="Количество")

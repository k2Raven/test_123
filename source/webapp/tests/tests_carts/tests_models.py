from django.test import TestCase

from webapp.models import Product, Cart, Category
from webapp.tests.factories.product import ProductFactory
from webapp.tests.factories.cart import CartFactory


class CartsModelTests(TestCase):

    def setUp(self):
        # self.product_1 = Product.objects.create(
        #     title='Product 1',
        #     category=self.category,
        #     price=100,
        #     qty=5,
        #     image='https://telefon.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2012/1-500x500.jpg'
        # )
        # self.product_2 = Product.objects.create(
        #     title='Product 2',
        #     category=self.category,
        #     price=300,
        #     qty=5,
        #     image='https://telefon.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2012/1-500x500.jpg'
        # )
        # self.product_3 = Product.objects.create(
        #     title='Product 3',
        #     category=self.category,
        #     price=200,
        #     qty=5,
        #     image='https://telefon.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2012/1-500x500.jpg'
        # )
        # self.product_1 = ProductFactory.create(price=100, qty=5)
        # self.product_2 = ProductFactory.create(price=300, qty=5)
        # self.product_3 = ProductFactory.create(price=200, qty=5)
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # cls.category = Category.objects.create(title='Test Category')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_get_full_total(self):
        # Cart.objects.create(product=self.product_1, qty=2)
        # Cart.objects.create(product=self.product_2, qty=1)
        # Cart.objects.create(product=self.product_3, qty=3)
        products = ProductFactory.create_batch(3, price=200, qty=4)
        for product in products:
            CartFactory.create(product=product, qty=2)
        result = Cart.get_full_total()
        self.assertEqual(1200, result)


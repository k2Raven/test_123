from django.test import TestCase
from http import HTTPStatus

from webapp.models import Category, Product
from webapp.tests.factories.category import CategoryFactory
from webapp.tests.factories.product import ProductFactory


class ProductsViewsTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = CategoryFactory.create()
        cls.correct_data = {
            'title': 'Product 1',
            'category': cls.category.id,
            'price': 100,
            'qty': 5,
            'image': 'https://telefon.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2012/1-500x500.jpg'
        }

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_products_create_view(self):
        response = self.client.post('/products/add/', data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().title, 'Product 1')

    def test_products_create_not_category_view(self):
        data = {
            'title': 'Product 1',
            'price': 100,
            'qty': 5,
            'image': 'https://telefon.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2012/1-500x500.jpg'
        }
        response = self.client.post('/products/add/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(Product.objects.count(), 0)

    def test_products_update_view(self):
        product = ProductFactory.create(title='Product qwerty')
        response = self.client.post(f'/products/{product.pk}/update/', data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # print(Product.objects.count())
        self.assertEqual(Product.objects.first().title, 'Product 1')

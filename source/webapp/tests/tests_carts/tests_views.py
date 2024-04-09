from django.contrib.auth import get_user_model
from django.test import TestCase
from http import HTTPStatus

from webapp.models import Category, Product
from webapp.tests.factories.category import CategoryFactory
from webapp.tests.factories.product import ProductFactory

User = get_user_model()


class CartViewsTest(TestCase):

    def setUp(self):
        self.product = ProductFactory.create(qty=3)
        user, created = User.objects.get_or_create(username='user')
        if created:
            user.is_superuser = True
            user.set_password('user')
            user.save()
        self.client.login(username='user', password='user')

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_products_add_to_cart_view(self):
        self.assertIsNone(self.client.session.get('cart'))
        self.client.get(f'/products/{self.product.pk}/add_to_cart/')
        self.assertIsNotNone(self.client.session.get('cart'))
        self.assertDictEqual(self.client.session.get('cart'), {str(self.product.pk): 1})

        self.client.get(f'/products/{self.product.pk}/add_to_cart/')
        self.assertDictEqual(self.client.session.get('cart'), {str(self.product.pk): 2})

        self.client.get(f'/products/{self.product.pk}/add_to_cart/')
        self.assertDictEqual(self.client.session.get('cart'), {str(self.product.pk): 3})

        self.client.get(f'/products/{self.product.pk}/add_to_cart/')
        self.assertDictEqual(self.client.session.get('cart'), {str(self.product.pk): 3})

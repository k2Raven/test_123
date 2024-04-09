import factory
from factory.django import DjangoModelFactory

from webapp.models import Cart
from webapp.tests.factories.product import ProductFactory


class CartFactory(DjangoModelFactory):
    product = factory.SubFactory(ProductFactory)
    qty = factory.Faker('pyint', min_value=1, max_value=4)

    class Meta:
        model = Cart

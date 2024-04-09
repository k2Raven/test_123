import factory
from factory.django import DjangoModelFactory

from webapp.models import Product
from webapp.tests.factories.category import CategoryFactory


class ProductFactory(DjangoModelFactory):
    title = factory.Sequence(lambda n: f'Product {n}')
    price = factory.Faker('pyint', min_value=100, max_value=500)
    qty = factory.Faker('pyint', min_value=1, max_value=10)
    image = 'https://telefon.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2012/1-500x500.jpg'
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product

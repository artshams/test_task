from django.test import TestCase
from django.test.client import RequestFactory
from djangoProject.factories import ProductsFactory, CategoriesFactory
from djangoProject.calls import get_pairs, get_products, get_categories
import json


class TestApiCalls(TestCase):
    def setUp(self):
        ProductsFactory.reset_sequence(1)
        CategoriesFactory.reset_sequence(1)
        cat1 = CategoriesFactory()
        cat2 = CategoriesFactory()
        cat3 = CategoriesFactory()
        ProductsFactory.create(categories=(cat1, cat2, cat3))
        ProductsFactory.create(categories=(cat1, cat3))
        ProductsFactory.create(categories=(cat2, cat3))
        ProductsFactory.create(categories=(cat2, cat3))
        ProductsFactory.create(categories=(cat2, cat3))
        ProductsFactory.create(categories=(cat1, cat2))

        self.factory = RequestFactory()
        self.request = self.factory.get('/')

    def test_get_categories(self):
        categories = json.loads(get_categories(self.request).content.decode("UTF-8"))
        self.assertEqual(len(categories["Group #1"]), 3)
        self.assertEqual(len(categories["Group #2"]), 5)
        self.assertEqual(len(categories["Group #3"]), 5)

    def test_get_products(self):
        products = json.loads(get_products(self.request).content.decode("UTF-8"))
        self.assertListEqual(products["Product #1"], ['Group #1', 'Group #2', 'Group #3'])
        self.assertListEqual(products["Product #2"], ['Group #1', 'Group #3'])

    def test_get_pairs(self):
        products = json.loads(get_pairs(self.request).content.decode("UTF-8"))
        self.assertEqual(products[0]['categories'], 1)
        self.assertEqual(products[1]['categories'], 2)
        self.assertEqual(products[2]['categories'], 3)
        self.assertEqual(products[3]['categories'], 1)

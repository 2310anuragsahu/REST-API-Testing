from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):

    def test_create_item(self):
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 19.99)

    def test_json(self):
        item = ItemModel('test', 19.99, 1)
        expected = {'name': 'test', 'price': 19.99}

        self.assertDictEqual(item.json(), expected)

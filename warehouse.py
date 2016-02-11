from collections import defaultdict
from product import *

class Warehouse(object):
	def __init__(self,_id,x,y,products):
		self.id = _id
		self.x = x
		self.y = y
		self.products = products

	def add_product(self, product, amount):
		self.products[product] += amount

	def remove_product(self, product, amount):
		self.products[product] -= amount

	def get_product_amount(self, product):
		return self.products[product];

	def calculate_weight(self):
		total = 0
		for key in self.products.keys():
			total += self.products[key]
		return total

	def __hash__(self):
		return hash([self.x, self.y, self.products])


import unittest

class TestAll(unittest.TestCase):
	def test_empty_drone_has_0_weight(self):
		drone = Warehouse(0, 0,0,defaultdict(int))
		self.assertEqual(0, drone.calculate_weight())

	def test_drone_has_weight_one_product(self):
		drone = Warehouse(0, 0,0,defaultdict(int))
		drone.add_product(Product(0, 10),1)
		self.assertEqual(1, drone.calculate_weight())

	def test_drone_has_weight_two_products(self):
		drone = Warehouse(0, 0,0,defaultdict(int))
		drone.add_product(Product(0, 10),1)
		drone.add_product(Product(0, 10),1)
		self.assertEqual(2, drone.calculate_weight())

	def test_drone_loses_weight(self):
		drone = Warehouse(0, 0,0,defaultdict(int))
		drone.add_product(Product(0, 10),2)
		drone.remove_product(Product(0, 10),1)
		self.assertEqual(1, drone.calculate_weight())

if __name__ == "__main__":
	unittest.main()
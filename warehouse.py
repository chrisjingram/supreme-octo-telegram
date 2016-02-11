from collections import defaultdict

class Warehouse(object):
	def __init__(self,x,y,products):
		self.x = x
		self.y = y
		self.products = defaultdict(int)

	def add_product(self, product, amount):
		self.products[product] += amount

	def remove_product(self, product, amount):
		self.products[product] -= amount

	def calculate_weight(self):
		total = 0
		for key in self.products.keys():
			total += self.products[key]
		return total


import unittest

class TestAll(unittest.TestCase):
	def test_empty_drone_has_0_weight(self):
		drone = Warehouse(0,0,0)
		self.assertEqual(0, drone.calculate_weight())

	def test_drone_has_weight_one_product(self):
		drone = Warehouse(0,0,1)
		drone.add_product(1,1)
		self.assertEqual(1, drone.calculate_weight())

	def test_drone_has_weight_two_products(self):
		drone = Warehouse(0,0,1)
		drone.add_product(1,1)
		drone.add_product(1,1)
		self.assertEqual(2, drone.calculate_weight())

	def test_drone_loses_weight(self):
		drone = Warehouse(0,0,1)
		drone.add_product(1,2)
		drone.remove_product(1,1)
		self.assertEqual(1, drone.calculate_weight())

print "--------------------"
unittest.main()
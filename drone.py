from collections import defaultdict
from product import *

class Drone(object):

	def __init__(self, _id, x, y, capacity):
		self.id = _id
		self.x = x
		self.y = y
		self.capacity = capacity
		self.products = defaultdict(int)

	def add_product(self, product, amount):
		new_weight = self.calculate_weight() + product.weight
		if(new_weight <= self.capacity):
			self.products[product] += amount
			return True
		else:
			return False

	def remove_product(self, product, amount):
		self.products[product] -= amount

	def calculate_weight(self):
		total = 0
		for key in self.products.keys():
			total += self.products[key] * key.weight
		return total


import unittest

class TestDrone(unittest.TestCase):
	def test_empty_drone_has_0_weight(self):
		drone = Drone(0,0,0,0)
		self.assertEqual(0, drone.calculate_weight())

	def test_drone_has_weight_one_product(self):
		drone = Drone(0,0,0,1)
		drone.add_product(Product(0, 1),1)
		self.assertEqual(1, drone.calculate_weight())

	def test_drone_has_weight_two_products(self):
		drone = Drone(0,0,0,2)
		self.assertEqual(True,drone.add_product(Product(0, 1), 1))
		self.assertEqual(True,drone.add_product(Product(0, 1), 1))
		self.assertEqual(2, drone.calculate_weight())

	def test_drone_can_calculate_weight_of_differently_sized_products(self):
		drone = Drone(0,0,0,10)
		drone.add_product(Product(0, 4), 1)
		drone.add_product(Product(0, 5), 1)
		self.assertEqual(9, drone.calculate_weight())


	def test_drone_loses_weight(self):
		drone = Drone(0,0,0,1)
		drone.add_product(Product(0, 1), 2)
		drone.remove_product(Product(0, 1), 1)
		self.assertEqual(1, drone.calculate_weight())

	def test_drone_does_not_add_product_when_full(self):
		drone = Drone(0,0,0,5)
		drone.add_product(Product(0, 5), 1)
		self.assertEqual(False, drone.add_product(Product(0, 1), 1))
		self.assertEqual(5, drone.calculate_weight())

if __name__ == "__main__":
	unittest.main()
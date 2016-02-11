from drone import *
from product import *
from warehouse import *
from order import *
import math

class Simulation():
	def __init__(self, drones, warehouses):
		self.drones = drones
		self.warehouses = warehouses

	def tick(self):
		pass

	def load_products_from_warehouse_to_drone(self, warehouse, drone, product, amount):
		# If multithreaded, add a lock here
		drone.add_product(product, amount)
		warehouse.remove_product(product, amount)

	def unload_products_from_drone_to_order(self, drone, order, product, amount):
		drone.remove_product(product, amount)
		# Order may want to show collection

	def calculate_minimum_turns(self, drone, order):
		turns = 0

		product = order.products.keys()[0]
		amount = order.products[product]

		# Find closest warehouse for item p
		warehouse = self.warehouses[0] # replace
		self.load_products_from_warehouse_to_drone(warehouse, drone, product, amount)
		turns += 1

		# Go to order location
		distance = euclidean_distance(drone.x, drone.y, order.x, order.y)
		turns_for_distance = int(math.ceil(distance))
		turns += turns_for_distance

		# Drop order
		self.unload_products_from_drone_to_order(drone, order, product, amount)
		turns += 1

		return turns

	


def euclidean_distance(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

import unittest

class TestSimulation(unittest.TestCase):
	def test_we_can_load_items_from_a_warehouse_to_a_drone(self):
		drone = Drone(0, 0, 50)
		product = Product(0, 10);
		products = {}
		products[product] = 10
		warehouse = Warehouse(0, 0, products)

		self.assertEqual(0, drone.calculate_weight())
		self.assertEqual(10, warehouse.get_product_amount(product))

		sim = Simulation([drone], [warehouse])
		sim.load_products_from_warehouse_to_drone(warehouse, drone, product, 5)

		self.assertEqual(50, drone.calculate_weight())
		self.assertEqual(5, warehouse.get_product_amount(product))

	def test_we_can_complete_example_1(self):
		drone = Drone(1, 3, 1000)
		product_p = Product(0, 5)

		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(1, 3, products_0)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(1, 4, order_0_products)

		sim = Simulation([drone], [warehouse_0])

		self.assertEqual(3, sim.calculate_minimum_turns(drone, order_0))

	def test_we_can_complete_example_1_but_with_different_order_location(self):
		drone = Drone(1, 3, 1000)
		product_p = Product(0, 5)

		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(1, 3, products_0)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(7, 12, order_0_products)

		sim = Simulation([drone], [warehouse_0])

		self.assertEqual(13, sim.calculate_minimum_turns(drone, order_0))

	def test_basic_euclidean(self):
		self.assertEqual(5, euclidean_distance(0, 0, 3, 4))

if __name__ == "__main__":
	unittest.main()
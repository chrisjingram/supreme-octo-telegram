from drone import *
from product import *
from warehouse import *

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

if __name__ == "__main__":
	unittest.main()
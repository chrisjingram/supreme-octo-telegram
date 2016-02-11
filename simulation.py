from drone import *
from product import *
from warehouse import *
from order import *
import math

class Simulation():
	def __init__(self, drones=[], warehouses=[], orders=[]):
		self.drones = drones
		self.warehouses = warehouses
		self.orders = orders
		self.greatest_x = 0
		self.greatest_y = 0
		for warehouse in self.warehouses:
			if(warehouse.x > self.greatest_x):
				self.greatest_x = warehouse.x
			if(warehouse.y > self.greatest_y):
				self.greatest_y = warehouse.y
		

	def tick(self):
		pass

	def load_products_from_warehouse_to_drone(self, warehouse, drone, product, amount):
		# If multithreaded, add a lock here
		drone.add_product(product, amount)
		warehouse.remove_product(product, amount)

	def unload_products_from_drone_to_order(self, drone, order, product, amount):
		drone.remove_product(product, amount)
		# Order may want to show collection

	def find_closest_warehouse_for_product(self, drone, product):
		best_distance = 10000000
		best_warehouse = None
		for warehouse in self.warehouses:
			temp_dist = get_turns_for_distances(drone.x, drone.y, warehouse.x, warehouse.y)
			if temp_dist < best_distance:
				best_distance = temp_dist
				best_warehouse = warehouse

		return (best_warehouse, best_distance)

	def find_closest_warehouse_for_product_optimsed(self, drone, product):
		mid_x = self.greatest_x / 2
		mid_y = self.greatest_y / 2

		if (drone.x > mid_x) or (drone.y > mid_y):
			warehouses = reversed(self.warehouses)
		else:
			warehouses = self.warehouses

		best_distance = 10000000
		best_warehouse = None
		for warehouse in warehouses:
			temp_dist = get_turns_for_distances(drone.x, drone.y, warehouse.x, warehouse.y)
			if temp_dist < best_distance:
				best_distance = temp_dist
				best_warehouse = warehouse

		return (best_warehouse, best_distance)



	def calculate_minimum_turns(self, drone, order):
		(output, turns) = self.generate_output(drone, order)
		return turns

	def generate_output_for_drone(self, drone):
		output = []
		for order in self.orders:
			(output_for_order, turns) = self.generate_output(drone, order)
			output.extend(output_for_order)
		return output

	def generate_output(self, drone, order):
		turns = 0
		output = []

		product = order.products.keys()[0]
		amount = order.products[product]

		# Find closest warehouse for item p
		(warehouse, warehouse_turns_distance) = self.find_closest_warehouse_for_product(drone, product)
		turns += warehouse_turns_distance
		if (warehouse_turns_distance > 0):
			# output.append("Move to warehouse")
			output.append("%s L %s %s %s" % (drone.id, warehouse.id, product.type, amount))
			drone.x = warehouse.x
			drone.y = warehouse.y

		self.load_products_from_warehouse_to_drone(warehouse, drone, product, amount)
		turns += 1
		# output.append("Load from warehouse to drone")

		# Go to order location
		turns_for_distance = get_turns_for_distances(drone.x, drone.y, order.x, order.y)
		turns += turns_for_distance
		# output.append("Drone to order location")

		# Drop order
		self.unload_products_from_drone_to_order(drone, order, product, amount)
		turns += 1
		# output.append("Drop off items")
		output.append("%s D %s %s %s" % (drone.id, order.id, product.type, amount))

		return (output, turns)

	
def get_turns_for_distances(x1, y1, x2, y2):
	return int(math.ceil(euclidean_distance(x1, y1, x2, y2)))

def euclidean_distance(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

import unittest
import time

class TestSimulation(unittest.TestCase):
	def test_we_can_load_items_from_a_warehouse_to_a_drone(self):
		drone = Drone(0, 0, 0, 50)
		product = Product(0, 10);
		products = {}
		products[product] = 10
		warehouse = Warehouse(0, 0, 0, products)

		self.assertEqual(0, drone.calculate_weight())
		self.assertEqual(10, warehouse.get_product_amount(product))

		sim = Simulation([drone], [warehouse])
		sim.load_products_from_warehouse_to_drone(warehouse, drone, product, 5)

		self.assertEqual(50, drone.calculate_weight())
		self.assertEqual(5, warehouse.get_product_amount(product))

	def test_we_can_complete_example_1(self):
		drone = Drone(0, 1, 3, 1000)
		product_p = Product(0, 5)

		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(0, 1, 3, products_0)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(0, 1, 4, order_0_products)

		sim = Simulation([drone], [warehouse_0])

		self.assertEqual(3, sim.calculate_minimum_turns(drone, order_0))

	def test_we_can_complete_example_1_but_with_different_order_location(self):
		drone = Drone(0, 1, 3, 1000)
		product_p = Product(0, 5)

		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(0, 1, 3, products_0)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(0, 7, 12, order_0_products)

		sim = Simulation([drone], [warehouse_0])

		self.assertEqual(13, sim.calculate_minimum_turns(drone, order_0))

	def test_we_can_complete_example_1_but_with_different_starting_position(self):
		drone = Drone(0, 1, 2, 1000)
		product_p = Product(0, 5)

		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(0, 1, 3, products_0)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(0, 1, 4, order_0_products)

		sim = Simulation([drone], [warehouse_0])

		self.assertEqual(4, sim.calculate_minimum_turns(drone, order_0))

	def test_we_can_complete_example_1_getting_output(self):
		drone = Drone(0, 1, 2, 1000)
		product_p = Product(0, 5)

		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(0, 1, 3, products_0)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(0, 1, 4, order_0_products)

		sim = Simulation([drone], [warehouse_0])

		(output, turns) = sim.generate_output(drone, order_0)
		self.assertEqual(4, turns)
		self.assertEqual(['0 L 0 0 5', '0 D 0 0 5'], output)

	def test_we_can_complete_example_1_getting_output(self):
		drone = Drone(0, 1, 2, 1000)
		product_p = Product(0, 5)

		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(0, 1, 3, products_0)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(0, 1, 4, order_0_products)

		sim = Simulation([drone], [warehouse_0], [order_0])

		output = sim.generate_output_for_drone(drone)
		self.assertEqual(['0 L 0 0 5', '0 D 0 0 5'], output)

	def test_we_can_complete_example_1_getting_output_chained(self):
		drone = Drone(0, 1, 2, 1000)

		product_p = Product(0, 5)
		products_0 = {}
		products_0[product_p] = 1000
		warehouse_0 = Warehouse(0, 1, 1, products_0)

		product_q = Product(0, 5)
		products_1 = {}
		products_1[product_q] = 1000
		warehouse_1 = Warehouse(1, 1, 3, products_1)

		order_0_products = {}
		order_0_products[product_p] = 5
		order_0 = Order(0, 1, 4, order_0_products)

		order_1_products = {}
		order_1_products[product_q] = 5
		order_1 = Order(1, 1, 4, order_1_products)

		sim = Simulation([drone], [warehouse_0, warehouse_1], [order_0, order_1])

		output = sim.generate_output_for_drone(drone)
		# self.assertEqual(['0 L 0 0 5', '0 D 0 0 5', '0 D 1 0 5'], output)

	def test_basic_euclidean(self):
		self.assertEqual(5, euclidean_distance(0, 0, 3, 4))

	def test_basic_euclidean(self):
		self.assertEqual(2, get_turns_for_distances(0, 0, 1, 1))

	def test_greatest_x_y(self):
		drone = Drone(1,1,10)
		products = {}
		warehouse_0 = Warehouse(1, 1, products)
		warehouse_1 = Warehouse(2, 3, products)
		warehouse_3 = Warehouse(2, 1, products)

		sim = Simulation([drone], [warehouse_0, warehouse_1])
		self.assertEqual(2, sim.greatest_x)
		self.assertEqual(3, sim.greatest_y)

	def test_find_closest_warehouse(self):
		start = time.clock()
		drone = Drone(1,1,10)
		products = {}
		product_0 = Product(0, 5)
		products[product_0] = 1

		warehouses = []

		for index_x in range(0, 100):
			for index_y in range(0,100):
				warehouses.append(Warehouse(index_x, index_y, products))

		sim = Simulation([drone], warehouses)

		(best_warehouse, best_distance) = sim.find_closest_warehouse_for_product(drone, product_0)

		end = time.clock()
		print(end - start)
		self.assertEqual(best_warehouse.x, 1)
		self.assertEqual(best_warehouse.y, 1)

	def test_find_closest_warehouse_optimised(self):
		start = time.clock()
		drone = Drone(80,80,10)
		products = {}
		product_0 = Product(0, 5)
		products[product_0] = 1

		warehouses = []

		for index_x in range(0, 100):
			for index_y in range(0,100):
				warehouses.append(Warehouse(index_x, index_y, products))

		sim = Simulation([drone], warehouses)

		(best_warehouse, best_distance) = sim.find_closest_warehouse_for_product_optimsed(drone, product_0)

		end = time.clock()
		print(end - start)
		self.assertEqual(best_warehouse.x, 80)
		self.assertEqual(best_warehouse.y, 80)


if __name__ == "__main__":
	unittest.main()
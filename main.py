print 'hello world'

from product import *
from drone import *
from warehouse import *
from order import *

FILENAME = 'easy_day_at_the_office.in'
import pprint

import unittest

def parse(filename):
	with open(filename, 'r') as f:
		return f.read().split('\n')

def extract_params(line):
	nums = line.split(' ')
	return {
		'rows': int(nums[0]),
		'cols': int(nums[1]),
		'D': int(nums[2]),
		'deadline': int(nums[3]),
		'max_load': int(nums[4])
	}

def extract_warehouse(warehouse, product_weights):
	xy = warehouse[0].split(' ')
	print xy
	products = {}
	product_quantities = warehouse[1].split(' ')
	for t in range(len(product_quantities)):
		products[Product(t, product_weights[t])] = product_quantities[t]
	return Warehouse(xy[0], xy[1], products)

def extract_warehouses(num_warehouses, warehouses, product_weights):
	warehouses = warehouses[0:int(num_warehouses)*2:2]
	print warehouses
	warehouse_objects = []

# TODO: keep track of highest and lowest xys
	for w in range(0, len(warehouses), 2):
		warehouse_objects.append(extract_warehouse([warehouses[w], warehouses[w+1]], product_weights))

	return warehouse_objects

def extract_product_weights(num_product_types, product_weights):
	products = {}
	product_weights = product_weights.split(' ')
	for i in range(int(num_product_types)):
		products[i] = product_weights[i]
	return products

def main():
	data = parse(FILENAME)
	params = extract_params(data[0])
	product_weights = extract_product_weights(data[1], data[2])

	warehouses = extract_warehouses(data[3], data[4:4+2*int(data[3])], product_weights)

	print warehouses
	print 'l'

if __name__ == "__main__":
	main()

class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

"""
	def test_warehouse(self):
		self.assertEqual(extract_warehouse(['0 0', '5 1 0']).__hash__(), Warehouse([]))
		extract_warehouse(Warehouse, ['0 0', '5 1 0'])
"""
print "--------------------"

unittest.main()
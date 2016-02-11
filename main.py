print 'hello world'

from product import *
from drone import *
from warehouse import *
from order import *

FILENAME = 'easy_day_at_the_office.in'

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

def extract_warehouses(num_warehouses, warehouses, product_weights):
	warehouses = warehouses[0:int(num_warehouses)*2:2]

	for w in range(len(warehouses)):# TODO: keep track of highest and lowest xys
		print warehouses[w]
		xy = warehouses[w].split(' ')
		print xy
		products = {}
		product_quantities = warehouses[w][1].split(' ')
		for t in range(len(product_quantities)):
			products[Product(t, product_weights[t])] = product_quantities[t]
		warehouses[w] = Warehouse(xy[0], xy[1], products)

	return warehouses

def extract_product_weights(num_product_types, product_weights):
	products = {}
	product_weights = product_weights.split(' ')
	for i in range(int(num_product_types)):
		products[i] = product_weights[i]
	return products

if __name__ == "__main__":
	data = parse(FILENAME)
	params = extract_params(data[0])
	product_weights = extract_product_weights(data[1], data[2])

	warehouses = extract_warehouses(data[3], data[4:4+2*int(data[3])], product_weights)
	print warehouses

	print product_weights
	print 'l'


class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"

unittest.main()
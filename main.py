print 'hello world'

import product
import drone
import warehouse
import order

FILENAME = 'busy_day.in'

import unittest

def parse(filename):
	with open(filename, 'r') as f:
		return f.read().split('\n')

def extract_params(line):
	nums = line.split(' ')
	return {
		'rows': float(nums[0]),
		'cols': float(nums[1]),
		'D': float(nums[2]),
		'deadline': float(nums[3]),
		'max_load': float(nums[4])
	}

def extract_products(num_product_types, product_weights):
	products = {}
	product_weights = product_weights.split(" ")
	for i in range(int(num_product_types)):
		products[str(i)] = product_weights[i]
	return products

if __name__ == "__main__":
	data = parse(FILENAME)
	params = extract_params(data[0])
	product_weights = extract_products(data[1], data[2])

	print params
	print product_weights
	print 'l'


class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"

unittest.main()
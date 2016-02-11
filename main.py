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

if __name__ == "__main__":
	data = parse(FILENAME)
	params = extract_params(data[0])



	print params
	print 'l'


class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"

unittest.main()
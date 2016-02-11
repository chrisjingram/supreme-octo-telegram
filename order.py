from collections import defaultdict
class Order(object):
	def __init__(self,x,y,products):
		self.products = products # dictionary
		self.x = x
		self.y = y


import unittest

class TestAll(unittest.TestCase):
	def test_construct_one_product(self):
		products = defaultdict(int)
		products[1] = 1
		order = Order(1,1,products)
		self.assertEqual(1,products[1])

print "--------------------"
if __name__ == "__main__":
	unittest.main()
from collections import defaultdict
class Order(object):
	def __init__(self,_id,x,y,products):
		self.id = _id
		self.products = products # dictionary
		self.x = x
		self.y = y


import unittest

class TestOrder(unittest.TestCase):
	def test_construct_one_product(self):
		products = defaultdict(int)
		products[1] = 1
		order = Order(0, 1,1,products)
		self.assertEqual(1,products[1])

print "--------------------"
if __name__ == "__main__":
	unittest.main()
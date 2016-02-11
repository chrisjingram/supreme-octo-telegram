print 'hello world'

class Warehouse(object):
	def __init__(self,x,y,products):
		self.x = x
		self.y = y
		self.products = products

class Drone(object):
	def __init__(self,x,y,capacity):
		self.x = x
		self.y = y
		self.capacity = capacity

class Product(object):
	def __init__(self,type,weight):
		self.type = type
		self.weight = weight

class Order(object):
	def __init__(self,x,y,products):
		self.products = products # dictionary
		self.x = x
		self.y = y





import unittest

class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"
unittest.main()
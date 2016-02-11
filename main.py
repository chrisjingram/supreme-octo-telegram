import unittest

print 'hello world'

class Warehouse(object):
	def __init__(self):
		pass

class Drone(object):
	def __init__(self):
		pass

class Product(object):
	def __init__(self):
		pass

class Order(object):
	def __init__(self):
		pass







class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"
unittest.main()
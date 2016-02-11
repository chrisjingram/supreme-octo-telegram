print 'hello world'

import product
import drone
import warehouse
import order





import unittest

class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"
unittest.main()

def parse():
	with open("datafile.txt", "r") as f:
		return f.read()

if __name__ == "__main__":
	data = parse()
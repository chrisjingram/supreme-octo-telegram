import unittest

class TestAllExample(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"
if __name__ == "__main__":
	unittest.main()
import unittest

print 'hello world'









class TestAll(unittest.TestCase):
	def test_first(self):
		self.assertEqual('hi', 'hi')

print "--------------------"
unittest.main()
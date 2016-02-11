class Product(object):
	def __init__(self,type_,weight):
		self.type = type_
		self.weight = weight

	def __hash__(self):
		return hash((self.type, self.weight))

	def __eq__(self, other):
		return (self.type, self.weight) == (other.type, other.weight)
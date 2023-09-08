class Table:
	def __init__(self):
		self.length = 100
		self.values = [None for _ in range(self.length)]
	
	def get_hash(self, key):
		return key % self.length
	
	def __setitem__(self, key, value):
		index = self.get_hash(key)
		self.values[index] = value
	
	def __getitem__(self, key):
		index = self.get_hash(key)
		return self.values[index]

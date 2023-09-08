class HashTable:
	def __init__(self):
		self.length = 100
		self.values = [None for _ in range(self.length)]
	
	def get_hash(self, key):
		return key % self.length
	
	def __setitem__(self, key, value):
		index = self.get_hash(key)
		self.values[index] = [key, value]
	
	def __getitem__(self, key):
		index = self.get_hash(key)
		return self.values[index][1]
	

class HashTableLinearProbing:
	def __init__(self):
		self.length = 100
		self.values = [None for _ in range(self.length)]
	
	def get_hash(self, key):
		index = key % self.length
		while self.values[index]:
			if self.values[index][0] == key:
				return index
			index = (index + 1) % self.length
		return index

	def __setitem__(self, key, value):
		index = self.get_hash(key)
		self.values[index] = [key, value]
	
	def __getitem__(self, key):
		index = self.get_hash(key)
		return self.values[index][1]


class HashTableQuadraticProbing:
	def __init__(self):
		self.length = 100
		self.values = [None for _ in range(self.length)]
	
	def get_hash(self, key):
		index = key % self.length
		if not self.values[index]:
			return index
		if self.values[index][0] == key:
			return index
		i = 1
		new_index = (index + 1) % self.length
		while self.values[new_index]:
			if self.values[new_index][0] == key:
				return new_index
			i += 1
			new_index = (index + (i**2)) % self.length
		return new_index

	def __setitem__(self, key, value):
		index = self.get_hash(key)
		self.values[index] = [key, value]
	
	def __getitem__(self, key):
		index = self.get_hash(key)
		return self.values[index][1]


class HashTableDoubleHash:
	def __init__(self):
		self.length = 100
		self.double = 61
		self.values = [None for _ in range(self.length)]
	
	def get_hash(self, key):
		index = key % self.length
		if not self.values[index]:
			return index
		if self.values[index][0] == key:
			return index
		internal_hash = self.double - (key % self.double)
		i = 1
		new_index = (index + internal_hash) % self.length
		while self.values[new_index]:
			if self.values[new_index][0] == key:
				return new_index
			i += 1
			new_index = (index + (i*internal_hash)) % self.length
		return new_index

	def __setitem__(self, key, value):
		index = self.get_hash(key)
		self.values[index] = [key, value]
	
	def __getitem__(self, key):
		index = self.get_hash(key)
		return self.values[index][1]

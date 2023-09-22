def sort(array):
	count = [0] * (max(array) + 1)
	for i in array:
		count[i] += 1
	array = []
	for i, val in enumerate(count):
		array += [i] * val
	return array

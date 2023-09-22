def sort(array):
	n = len(array)
	for i in range(1, n):
		value = array[i]
		for j in range(i-1, -1, -1):
			if value >= array[j]:
				array[j+1] = value
				break
			array[j+1] = array[j]
		else:
			array[0] = value
	return array

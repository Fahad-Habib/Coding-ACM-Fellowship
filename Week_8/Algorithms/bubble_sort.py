def sort(array):
	n = len(array)
	for i in range(n):
		is_sorted = True
		for j in range(n-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				is_sorted = False
		if is_sorted:
			break
	return array

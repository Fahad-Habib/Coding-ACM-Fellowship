def sort(array):
	n = len(array)
	for i in range(n):
		min_ind = i
		for j in range(i+1, n):
			if array[min_ind] > array[j]:
				min_ind = j
		array[i], array[min_ind] = array[min_ind], array[i]
	return array

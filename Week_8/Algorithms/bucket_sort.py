def insertion_sort(array):
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


def sort(array):
	n_buckets = 100
	buckets = [[] for _ in range(n_buckets)]
	for i in array:
		buckets[int(n_buckets*i)].append(i)
	for i in range(n_buckets):
		buckets[i] = insertion_sort(buckets[i])
	array = []
	for i in buckets:
		array += i
	return array

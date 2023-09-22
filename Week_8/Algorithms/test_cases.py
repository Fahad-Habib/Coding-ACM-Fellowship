import insertion_sort, bubble_sort, bucket_sort, count_sort, quick_sort, selection_sort, merge_sort
import random


def test_bubble(no_of_test_cases):
	print("\nTesting Bubble Sort:\n")
	for i in range(no_of_test_cases):
		print(f"Test Case {i+1}: ", end=' ')
		test_array = [random.randint(1, 1000) for _ in range(10 ** i)]
		sorted_array = bubble_sort.sort(test_array)
		test_array.sort()
		if sorted_array == test_array:
			print("Passed")
		else:
			print("Failed")


def test_insertion(no_of_test_cases):
	print("\nTesting Insertion Sort:\n")
	for i in range(no_of_test_cases):
		print(f"Test Case {i+1}: ", end=' ')
		test_array = [random.randint(1, 1000) for _ in range(10 ** i)]
		sorted_array = insertion_sort.sort(test_array)		
		test_array.sort()
		if sorted_array == test_array:
			print("Passed")
		else:
			print("Failed")



def test_selection(no_of_test_cases):
	print("\nTesting Selection Sort:\n")
	for i in range(no_of_test_cases):
		print(f"Test Case {i+1}: ", end=' ')
		test_array = [random.randint(1, 1000) for _ in range(10 ** i)]
		sorted_array = selection_sort.sort(test_array)		
		test_array.sort()
		if sorted_array == test_array:
			print("Passed")
		else:
			print("Failed")



def test_merge(no_of_test_cases):
	print("\nTesting Merge Sort:\n")
	for i in range(no_of_test_cases):
		print(f"Test Case {i+1}: ", end=' ')
		test_array = [random.randint(1, 1000) for _ in range(10 ** i)]
		sorted_array = merge_sort.sort(test_array)		
		test_array.sort()
		if sorted_array == test_array:
			print("Passed")
		else:
			print("Failed")



def test_quick(no_of_test_cases):
	print("\nTesting Quick Sort:\n")
	for i in range(no_of_test_cases):
		print(f"Test Case {i+1}: ", end=' ')
		test_array = [random.randint(1, 1000) for _ in range(10 ** i)]
		sorted_array = test_array[:]
		quick_sort.sort(sorted_array, 0, (10**i)-1)		
		test_array.sort()
		if sorted_array == test_array:
			print("Passed")
		else:
			print("Failed")



def test_counting(no_of_test_cases):
	print("\nTesting Counting Sort:\n")
	for i in range(no_of_test_cases):
		print(f"Test Case {i+1}: ", end=' ')
		test_array = [random.randint(1, 1000) for _ in range(10 ** i)]
		sorted_array = count_sort.sort(test_array)		
		test_array.sort()
		if sorted_array == test_array:
			print("Passed")
		else:
			print("Failed")



def test_bucket(no_of_test_cases):
	print("\nTesting Bucket Sort:\n")
	for i in range(no_of_test_cases):
		print(f"Test Case {i+1}: ", end=' ')
		test_array = [random.randint(1, 1000) / 1001 for _ in range(10 ** i)]
		sorted_array = bucket_sort.sort(test_array)		
		test_array.sort()
		if sorted_array == test_array:
			print("Passed")
		else:
			print("Failed")


test_bubble(5)
test_insertion(5)
test_selection(5)
test_merge(5)
test_quick(5)
test_counting(5)
test_bucket(5)

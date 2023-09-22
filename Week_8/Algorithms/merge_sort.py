def merge(a, b):
	c = []
	n = len(a) + len(b)
	while len(c) != n:
		if len(a) == 0 or len(b) == 0:
			if len(a) == 0 and len(b) != 0:
				c += b
			elif len(b) == 0 and len(a) != 0:
				c += a
		else:
		    if b[0] < a[0]:
		        c.append(b.pop(0))
		    else:
		        c.append(a.pop(0))
	return c


def sort(array):
	if len(array) == 1:
		return array
	return merge(sort(array[:len(array)//2]), sort(array[len(array)//2:]))

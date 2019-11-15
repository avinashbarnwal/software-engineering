# sanket - merge sort

"""
The following code is an implementation of merge sort.

We break the array into equal parts till we reach atomic
states. Once we reach the atomic states we merge the 
sub arrays in sorted way.

In the mergersort function we break the array into two
equal halves recursively and merge them in the same order
as their splits.

the complexity of this sort is O(nlogn)
"""

def merge(left,right):
	"""
	left: left array
	right: right array

	return: c: sorted merger of left and right
	"""
	c = []
	left = left[::-1]
	right = right[::-1]
	while left and right:
		if left[-1] > right[-1]:
			c.append(right.pop())
		else:
			c.append(left.pop())

	while left:
		c.append(left.pop())

	while right:
		c.append(right.pop())
	
	return c

def mergesort(arr):
	"""
	arr: input array to be sorted

	return: sorted array using merge sort
	"""
	if len(arr) == 1:
		return arr

	left = arr[:len(arr)//2]
	right = arr[len(arr)//2:]

	left = mergesort(left)
	right = mergesort(right)

	return merge(left,right)

if __name__ == '__main__':
	arr = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
	out = mergesort(arr)
	print(out)
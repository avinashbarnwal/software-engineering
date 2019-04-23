# sanket - quicksort

"""
The following code is an implementation of quicksort
using hoarse's partition. Where we move all the elements
less than the index to left and move all the elements
greater than pivot to right of pivot by swapping them
recursively.

For sorting we parition the array into two parts and
then recursively partition left and right arrays till
the array is sorted.

When the array is sorted the complexity of quicksort
degrades to O(n^2). It is an unstable sort(when two 
values are equal it swaps them).
"""

def partition(arr,left,right,pivot):
	"""
	Hoarse's partition scheme
	-------------------------
	arr: input array
	left: index of the left element
	right: index of the right element
	pivot: index of element to parition w.r.t

	return: index of left after partition
	"""
	while left<=right:
		while arr[left] < arr[pivot]:
			left+=1

		while arr[right] > arr[pivot]:
			right-=1

		if left<=right:
			arr[left],arr[right] = arr[right],arr[left]
			left+=1
			right-=1
	# return arr
	return left

def quicksort(arr,left,right):
	"""
	arr: input array
	left: 0
	right: len(arr) -1

	sorts the array inplace with quicksort
	"""
	if left>=right:
		return
	pivot = (left+right)//2
	ind_ex = partition(arr,left,right,pivot)
	quicksort(arr,left,ind_ex-1)
	quicksort(arr,ind_ex,right)


if __name__ == '__main__':
	arr = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
	# print(partition(arr,0,len(arr)-1,len(arr)//2))
	quicksort(arr,0,len(arr)-1)
	print(arr)
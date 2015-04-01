## Author   __viva fung__  ##

import array

class Solution_2():
	def binary_search(self, arr, value):
		left = 0
		right = len(arr) - 1
		NOT_FOUND = -1
		if len(arr) != 0 and value <= arr[left]:
			return NOT_FOUND
		if len(arr) == 0:
			return NOT_FOUND
		
		while left <= right:
			mid = left + (right - left)/2
			if arr[mid] < value:
				left = mid
			else:
				right = mid - 1
				return mid
		return NOT_FOUND




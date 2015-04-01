## Author   __viva fung__  ##

import array

class Solution_4():
	def distance(self, arr):
		if len(arr) != 2:
			raise ValueError("Invalid data...")
		return arr[1]-arr[0]+1

	def contiguous_largest_sum(self, arr):
		''' it is actually Kadane's algorithm that cost O(n) time complexity and O(1) space complexity.
		Scan through the array to compute maximum sub-sum at each position. 
		(1) All positive numbers -> largest sum is the sum of list
		(2) All negative numbers -> largest sum is the largest number in the list
		(3) Hybrid numbers -> once the current sum < 0, start point starts from i+1, reset sum to 0
		Create a hashmap to save all the index pair for largest sum, then compute which one has shortest legnth'''

		default_sum = 0
		max_sum = -10000
		start = end = 0
		index_results = []
		hashmap = {}

		if len(arr) == 0:
			return start, end, 0

		for i in xrange(0, len(arr) - 1):
			if default_sum >= 0:
				default_sum += arr[i]
			else:
				default_sum = arr[i]
				start = i 
			if default_sum > max_sum:
				max_sum = default_sum
				end = i 
			
			'''dealing the case when start and end are at same position'''
			if default_sum < 0:
				temp_max = default_sum
				''' Use temp_max to save the current max value to 
				dealing with the duplicate negative number in the array'''

				if temp_max == max_sum:
					start = end = i
				else:
					max_sum = default_sum
					default_sum = 0
					start = end = i + 1  

			iter_index = []
			iter_index.append(start)
			iter_index.append(end)
			index_results.append(iter_index)

			if max_sum not in hashmap.keys():
				hashmap[max_sum] = index_results[-1]
			else:
				hashmap[max_sum].append(index_results[-1])

		'''this line is simply for fix one of my mistake: somehow not all the elements in hashmap
		are list of index, some of them are int, this line of code is to erase the int value'''
		no_integers = [el for el in hashmap[max_sum] if not isinstance(el, int)]

		'''compute the distance for each array of index that have contiguous largest sum and find the shortest one'''
		distance_list = []
		for el in no_integers:
			distance_list.append(self.distance(el))
		try:
			val, idx = min((val, idx) for (idx, val) in enumerate(distance_list))
			start = no_integers[idx][0]
			end = no_integers[idx][1]
		except ValueError as e:
			'''when start and end point are the same, min() will return valueError'''
			return start, end, max_sum

		return start, end, max_sum











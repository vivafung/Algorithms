## Author __Viva Fung__ ##

from DNA_problem2 import Solution_2
from DNA_problem4 import Solution_4
import unittest

class sfung(unittest.TestCase):
	def test_binary_search_empty_list(self):
		arr = []
		val = 7
		res = Solution_2()
		results = res.binary_search(arr, val)
		self.assertEqual(results, -1)

	def test_binary_search_existing_value(self):
		arr = [1, 2, 3, 3, 4, 4, 7, 7, 8, 14, 15, 15]
		val = 14
		res = Solution_2()
		results = res.binary_search(arr, val)
		self.assertEqual(results, 9)

	def test_binary_search_last_value(self):
		arr = [1, 2, 3, 3, 4, 4, 7, 7, 8, 14, 15, 15]
		val = 15
		res = Solution_2()
		results = res.binary_search(arr, val)
		self.assertEqual(results, 10)

	def test_binary_search_nonexisting_value(self):
		arr = [1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 14, 15, 15]
		val = 13
		res = Solution_2()
		results = res.binary_search(arr, val)
		self.assertEqual(results, 11)

	def test_contiguous_lastest_sum_empty_list(self):
		arr = []
		res = Solution_4()
		a, b, results = res.contiguous_largest_sum(arr)
	
		self.assertEqual(a, 0)
		self.assertEqual(b, 0)
		self.assertEqual(results, 0)

	def test_contiguous_lastest_sum_mix_list(self):
		arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
		res = Solution_4()
		a, b, results = res.contiguous_largest_sum(arr)
	
		self.assertEqual(a, 3)
		self.assertEqual(b, 6)
		self.assertEqual(results, 6)


	def test_contiguous_lastest_sum_nagetive_list(self):
		arr = [-9, -22, -5, -5]
		res = Solution_4()
		a, b, results = res.contiguous_largest_sum(arr)
		
		self.assertEqual(a, 2)
		self.assertEqual(b, 2)
		self.assertEqual(results, -5)


	def test_contiguous_lastest_sum_positive_list(self):
		arr = [3, 0, -6, 16, 9, 43, -1, -100, 7, 57, 2, 2, -190]
		res = Solution_4()
		a, b, results = res.contiguous_largest_sum(arr)
		
		self.assertEqual(a, 3)
		self.assertEqual(b, 5)
		self.assertEqual(results, 68)


if __name__ == "__main__":
    unittest.main(verbosity=2)



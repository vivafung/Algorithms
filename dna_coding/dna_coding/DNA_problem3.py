# Author   __viva fung__  #
# Run $ python DNA_problem3.py inputfile.txt 567  in the terminal. The testing file contains 1212 lines

import random
import array
import sys, getopt

class Solution():
	def report_current_index(self, filename):
		'''For avoiding read all the data into memory, create generator to readline 
		and save the begining position of iterators by using .tell()'''

		start_index_list = []
		start_index_list.append(0)
		with open(filename, "r") as f:
			while f.readline():
				start_index_list.append(f.tell())

			'''Delete the last line index'''
			del start_index_list[-1]
		return len(start_index_list), start_index_list

	def print_target(self, file_object, index_list, num):
		'''Using .seek() to locate associated iterator position based on the target line.'''

		file_object.seek(index_list[num - 1], 0)
		target_line = file_object.readline().strip("\n")
		print "The target line is: " + target_line

	def is_valid_range(self, n, low, high):
		'''Check whether random number is within the range of the file'''

		return True if (n >= low and n <= high) else False

def main():
	obj = Solution()
	if len(sys.argv) == 3:
		try:
			filename = str(sys.argv[1])
			ran_num = int(sys.argv[2])
			print filename, ran_num
		except getopt.GetoptError as e:
			print "Parsing Error....."
			sys.exit(2)
	else:
		print "Please re-enter the correct filename or number of lines....."
		return False

	file_in = open(filename, "r")
	list_len, iter_index = obj.report_current_index(filename)

	if obj.is_valid_range(ran_num, 1, list_len):
		obj.print_target(file_in, iter_index, ran_num)
	else:
		raise ValueError
	
if __name__ == "__main__":
	main()



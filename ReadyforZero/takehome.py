 ## Author __Viva Fung__ ##

import array 
import binascii
import math
import itertools
import pickle
import random
import sys, getopt

class Solution(object):
	def import_binary_file(self, filename):
		file_in = open(filename, "rb")
		s = file_in.read()
		arr = []
		for i in xrange(0, len(s)):
			byte = ord(s[i])
			'''Default binary in python starts as "0b", 
			create function "bin" to clean data getting rid of 0b'''

			bin = lambda n : (n > 0) and (bin(n/2) + str(n%2)) or '' 
			bin_val = bin(byte).zfill(8)
			arr.append(bin_val)
		file_in.close()
		return arr

	def convert_string_to_decimal(self, string):
		result = 0
		for i in xrange(0, len(string)):
			if string[i] == '1':
				result += pow(2, len(string) - 1 - i)
		return result

	def encode_dna_moculer(self, dna_mapping, binary_board):
		nucleotide_results = []
		quality_score_results = []

		for item in binary_board:
			# Encode DNA nucleotide
			dna_nucleotide = dna_mapping[item[:2]]
			nucleotide_results.append(dna_nucleotide)

			# Encode quality score
			temp = self.convert_string_to_decimal(item[2:]) + 33
			quality_score = chr(temp)
			quality_score_results.append(quality_score)

		return nucleotide_results, quality_score_results


	def aggregate_sequence(self, size, input_sequence):
		results = []
		chunked_sequence = map(None, *([iter(input_sequence)] * size))
		for el in chunked_sequence:
			if not None in el:
				encoded_seq = "".join(el)
				results.append(encoded_seq)
		return results


	def output(self, size, nucl_res, quality_res):
		# Assert encoded_dna_list and encoded_quality_score have same length
		if self.assert_size(len(nucl_res), len(quality_res)):
			print "CORRECT!!!"
		else:
			raise ValueError('Wrong processing..... ')

		output_results = []
		'''data processing based on required output string length'''
		encoded_dna_list = self.aggregate_sequence(size, nucl_res)
		encoded_quality_score = self.aggregate_sequence(size, quality_res)

		for i in xrange(0, len(encoded_dna_list)):
			output_results.append("@READ_" + str(i + 1))
			output_results.append(encoded_dna_list[i])
			output_results.append("+READ_" + str(i + 1))
			output_results.append(encoded_quality_score[i])
		return output_results


	def assert_size(self, val_1, val_2):
		return True if (val_1 == val_2) else False


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
	'''Total computational complexity is O(n) that n = number of input bytes'''

	obj = Solution()
	CONST_L = 7
	dna_mapping = {"00" : "A", "01" : "C", "10" : "G", "11" : "T"}

	input_file = "Downloads/dna_conversion_samples/input"
	output_file = "Downloads/dna_conversion_samples/readyforzero_takehome"

	binary_board = obj.import_binary_file(input_file)
	nucleotide_results, quality_score_results = obj.encode_dna_moculer(dna_mapping, binary_board)
	pickle.dump(obj.output(CONST_L, nucleotide_results, quality_score_results), open(output_file, "w"))

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

	file_in = open(output_file, "r")
	list_len, iter_index = obj.report_current_index(output_file)

	if obj.is_valid_range(ran_num, 1, list_len):
		obj.print_target(file_in, iter_index, ran_num)
	else:
		raise ValueError


if __name__ == "__main__":
	main()

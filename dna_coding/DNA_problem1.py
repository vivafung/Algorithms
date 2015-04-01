 ## Author __Viva Fung__ ##

import array 
import binascii
import math
import itertools
import pickle

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


def main():
	'''Total computational complexity is O(n) that n = number of input bytes'''

	obj = Solution()
	CONST_L = 7
	dna_mapping = {"00" : "A", "01" : "C", "10" : "G", "11" : "T"}

	input_file = "Downloads/dna_conversion_samples/input"
	output_file = "Downloads/dna_conversion_samples/output_vivafung"

	binary_board = obj.import_binary_file(input_file)
	nucleotide_results, quality_score_results = obj.encode_dna_moculer(dna_mapping, binary_board)
	pickle.dump(obj.output(CONST_L, nucleotide_results, quality_score_results), open(output_file, "w"))


if __name__ == "__main__":
	main()
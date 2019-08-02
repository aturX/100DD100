#!/usr/bin/env python3 # For use on ELW B238 machines
# -*- coding: utf-8 -*-
# See https://www.python.org/dev/peps/pep-0263/ about encoding

import os
import sys


def encode_main():
	with open("test00.txt", "r", encoding="utf-8") as f:
		plain_text = f.read()
		# print("In encode_main", plain_text)
	dictionary = sorted(set(plain_text))
	# print("dictionary ({})".format(dictionary))
	# Transformation
	compressed_text = list()
	rank = 0
	# read in each character
	for c in plain_text:
		rank = dictionary.index(str(c))  # find the rank of the character in the dictionary
		# print("rank {}, char {}".format(rank,str(c)))
		compressed_text.append(str(rank))  # update the encoded text

		# update the dictionary
		dictionary.pop(rank)
		dictionary.insert(0, c)
	# print("end",dictionary)
	dictionary.sort()  # sort dictionary
	# print("end2", dictionary)
	print(compressed_text)
	# with open("test00.mtf", "w", encoding="utf-8") as f:
	# 	f.write(compressed_text)
	return (compressed_text, dictionary)


def decode_main(a):

	# with open("test00.mtf", "r", encoding="utf-8") as f:
	# 	compressed_data = f.read()
	compressed_data = a
	compressed_text = compressed_data[0]
	dictionary = list(compressed_data[1])

	plain_text = ""
	rank = 0
	# read in each character of the encoded text
	for i in compressed_text:
		# read the rank of the character from dictionary
		rank = int(i)
		plain_text += str(dictionary[rank])

		# update dictionary
		e = dictionary.pop(rank)
		dictionary.insert(0, e)

	return plain_text  # Return original string

command = os.path.basename(__file__)

# if __name__ == "__main__" and command == "text2mtf.py":
#  encode_main()
# elif __name__ == "__main__" and command == "mtf2text.py":
data = encode_main()
# print(data)
t = decode_main(data)
print(t)
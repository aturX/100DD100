
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
	with open("test00.mtf", "w", encoding="utf-8") as f:
		f.write(compressed_text)
	return (compressed_text, dictionary)



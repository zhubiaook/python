'''This module is used to sort by the frequency of the letter in the string.
Copyright: zhubiao
Date: 2018-03-18
'''

def make_histogram(s):
	'''Make a map from letters to number of times they appear in s.
	:param s: string
	:return: dictionary from letter to frequency
	'''
	hist = dict()
	for letter in s:
		hist[letter] = hist.get(letter,0)+1
	return hist


def most_frequent(s):
	'''Sorts the letters in s in reverse order of frequency.
	:param s: string
	:return: list of tuple include letter and frequency by sorted
	'''
	hist = make_histogram(s)
	t = list()
	for k,v in hist.items():
		t.append((v,k))

	t.sort(reverse=True)
	return t


def read_file(filename):
	'''Convert the contents of file to a string.
	:param filename: file name
	:return: string
	'''
	lines = open(filename)
	words = ''
	for line in lines:
		word = line.strip()
		words = words + word

	return words


if __name__ == '__main__':
	string = read_file('../words.txt')
	letter_sequence = most_frequent(string)
	for item in letter_sequence:
		print(item[1],item[0])
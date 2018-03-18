'''Find metathesis_pair words
Copyright: zhubiao
Date: 2018-03-18
'''
import anagrams

def metathesis_pair(d):
	for word1 in d:
		for word2 in d:
			if word1 < word2 and word_distance(word1, word2) == 2:
				print(word1, word2)

def word_distance(word1, word2):
	count = 0
	for letter1, letter2 in zip(word1, word2):
		if letter1 != letter2:
			count = count + 1

	return count

if __name__ == '__main__':
	word_dict = anagrams.anagrams('../words.txt')
	for line in word_dict:
		metathesis_pair(line)
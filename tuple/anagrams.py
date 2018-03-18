'''Find all anagrams in a list of words, Print the words by the order
'''
def anagrams(filename):
	d = dict()
	fn = open(filename)
	for lines in fn:
		word = lines.strip()
		sorted_word = ''.join(sorted(word))
		d[sorted_word] = d.get(sorted_word,[])
		d[sorted_word].append(word)

	t = []
	for w in d.values():
		w_len = len(w)
		if w_len > 1:
			t.append((w_len,w))

	t.sort(reverse=True)
	result = []
	for w1,w2 in t:
		result.append(w2)

	return result

word_dict = anagrams('../words.txt')
for anagram in word_dict:
	print(anagram)

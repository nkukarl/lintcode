'''
Thoughts:

Use res to record the current longest word(s)
Iterate through the dictionary, compare the current word with the words in res
If length of current word is longer, re-initialise res with current word
If lengths are equal, append current word to res
If length of current word is shorter, ignore

'''

class Solution:
	def longestWords(self, dictionary):
		if not dictionary:
			return []
		res = [dictionary[0]]
		for word in dictionary[1:]:
			if len(word) > len(res[-1]):
				res = [word]
			elif len(word) == len(res[-1]):
				res.append(word)
		return res


dictionary = ['dog', 'google', 'facebook', 'internationalization', 'blabla']
dictionary = ['like', 'love', 'hate', 'yes']

inst = Solution()
print(inst.longestWords(dictionary))
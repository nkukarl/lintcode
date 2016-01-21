class Solution:
	def hashCode(self, key, HASH_SIZE):
		key = key[::-1]
		rem = 1
		res = ord(key[0])
		for k in key[1:]:
			rem = (33 * rem) % HASH_SIZE
			res += (ord(k) * rem) % HASH_SIZE
		return res % HASH_SIZE

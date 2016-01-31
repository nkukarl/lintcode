'''
Thoughts:

Define getNeighbours() to get the neighbours of word from Dict, for each word, change each of its letters to a different letter, if the new word is different from the original word and the new word is in Dict, append it to neighbours and eventually return neighbours

Define isNeighbour() to determine whether two words are neighbours
If the two words are of different size, return False
Compare all the letters of word1 and word2, if the number of different letters (diff) is over 1, return False, otherwise, return True
N.B., if word1 == word2, diff == 0, True would be returned

The minimum ladder length is 1, hence, push [start, 1] to an empty queue []
While queue is not empty, do the following
Pop the first element of the queue to assign cur and length
If cur and end are neighbours, return length + 1
Otherwise, get the neighbours of cur from Dict
Append append each neighbour nb together with length + 1 to the queue
At the same time, remove nb from Dict

If nothing is returned after depleting queue, return 0 since no ladder can connect start with end by using Dict

'''

class Solution:
    def ladderLength(self, start, end, Dict):
        if not start or not end or not Dict:
            return 0
        queue = [[start, 1]]
        while queue:
            cur, length = queue.pop(0)
            if self.isNeighbour(cur, end):
                return length + 1
            neighbours = self.getNeighbours(cur, Dict)
            for nb in neighbours:
                queue.append([nb, length + 1])
                Dict.remove(nb)
        return 0
        
    def getNeighbours(self, word, Dict):
        n = len(word)
        chars = 'abcdefghijklmnopqrstuvwxyz'
        neighbours = []
        for i in range(n):
            for char in chars:
                tmp = list(word)
                tmp[i] = char
                tmp = ''.join(tmp)
                if tmp != word and tmp in Dict:
                    neighbours.append(tmp)
        return neighbours
        
    def isNeighbour(self, word1, word2):
        if len(word1) != len(word2):
            return False
        n = len(word1)
        diff = 0
        for i in range(n):
            if word1[i] != word2[i]:
                diff += 1
            if diff > 1:
                return False
        return True
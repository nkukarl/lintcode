class Edge:
    def __init__(self, pos, height, isStart):
        self.pos = pos
        self.height = height
        self.isStart = isStart

class MaxHeap:
    def __init__(self):
        self.A = []

    def push(self, m):
        self.A.append(m)
        self.__up(len(self.A) - 1)
        # print(self.A)

    def __up(self, i):
        n = len(self.A)
        if i <= 0 or i >= n:
            return
        parent = self.A[(i - 1) // 2]
        if self.A[i] > parent:
            self.A[i], self.A[(i - 1) // 2] = self.A[(i - 1) // 2], self.A[i]
            self.__up((i - 1) // 2)

    def pop(self):
        if self.A:
            self.A[-1], self.A[0] = self.A[0], self.A[-1]
            tmp = self.A.pop()
            self.__down(0)
            # print(self.A)
            return tmp
        

    def __down(self, i):
        n = len(self.A)
        if i >= n:
            return
        
        if 2 * i + 1 >= n:
            left = -2 ** 31
        else:
            left = self.A[2 * i + 1]
        
        if 2 * i + 2 >= n:
            right = -2 ** 31
        else:
            right = self.A[2 * i + 2]

        if left > right and left > self.A[i]:
            self.A[i], self.A[2 * i + 1] = self.A[2 * i + 1], self.A[i]
            self.__down(2 * i + 1)
        elif right > self.A[i]:
            self.A[i], self.A[2 * i + 2] = self.A[2 * i + 2], self.A[i]
            self.__down(2 * i + 2)


    def top(self):
        if self.A:
            return self.A[0]

    def remove(self, idx):
        newVal = self.A[-1]
        oldVal = self.A[idx]
        self.A[-1], self.A[idx] = self.A[idx], self.A[-1]
        self.A.pop()
        if oldVal > newVal:
            self.__down(idx)
        else:
            self.__up(idx)
        

class Solution:
    def buildingOutline(self, buildings):
        if not buildings:
            return []
        tmp = []
        for b in buildings:
            tmp.append(Edge(b[0], b[2], True))
            tmp.append(Edge(b[1], b[2], False))
        tmp.sort(key = lambda x: (x.pos, x.isStart))
        mh = MaxHeap()
        mh.push(0)
        res = []
        for t in tmp:
            if t.isStart:
                if t.height > mh.top():
                    res.append([t.pos, t.height])
                mh.push(t.height)
            else:
                oldMax = mh.top()
                idx = mh.A.index(t.height)
                mh.remove(idx)
                newMax = mh.top()
                if newMax != oldMax:
                    res.append([t.pos, mh.top()])
        # return res
        ans = []
        cur, h = res[0]
        for r in res[1:]:
            pos, height = r
            if h != 0 and cur != pos:
                ans.append([cur, pos, h])
            cur = pos
            h = height
        return ans



buildings = [[1, 3, 3], [2, 4, 4], [5, 6, 1]]
buildings = [[1, 3, 3], [2, 4, 4], [5, 8, 2], [6, 7, 4], [8, 9, 4]]
print(len(buildings))
inst = Solution()
res = inst.buildingOutline(buildings)

print(res)

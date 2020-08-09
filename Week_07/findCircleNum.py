class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        length = len(M)
        p = list(range(length))
        for i in range(length):
            for j in range(length):
                if M[i][j] == 0 or i == j: continue
                self.union(p, i, j)
        return len(set([self.parent(p, i) for i in range(length)]))

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p2] = p1

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i; i = p[i]; p[x] = i
        return root
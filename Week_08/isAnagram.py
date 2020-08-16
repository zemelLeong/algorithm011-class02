class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        a = {}
        b = {}
        for i, j in zip(s, t):
            a[i] = a.get(i, 0) + 1
            b[j] = b.get(j, 0) + 1
        return a == b
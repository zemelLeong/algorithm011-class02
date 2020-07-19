class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ans, gi, si = 0, 0, 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                ans += 1; gi += 1; si += 1
            else:
                si += 1
        return ans
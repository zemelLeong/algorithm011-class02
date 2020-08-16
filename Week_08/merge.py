class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = [intervals[0]]
        p = 1
        while p < len(intervals):
            if ans[-1][1] >= intervals[p][0]:
                lis = [*ans[-1], *intervals[p]]
                ans[-1] = [min(lis), max(lis)]
            else:
                ans.append(intervals[p])

            p += 1

        return ans
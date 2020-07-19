class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_reachable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= end_reachable: end_reachable = i

        return end_reachable == 0
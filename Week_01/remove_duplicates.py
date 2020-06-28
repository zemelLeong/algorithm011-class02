class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        mem = nums[0]
        index = 1
        while index < len(nums):
            if mem == nums[index]:
                nums.pop(index)
            else:
                mem = nums[index]
                index += 1

        return len(nums)
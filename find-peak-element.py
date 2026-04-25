class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l, h = 0, len(nums) - 1
        while l <= h:
            if nums[l] > nums[l + 1]:
                return l
            elif nums[h] > nums[h - 1]:
                return h
            l +=1
            h -=1

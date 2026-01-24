class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            if num in seen:
                return [idx, seen[num][1]]
            seen[target - num] = num, idx

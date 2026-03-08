class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = list(dict.fromkeys(nums))
        if len(distinct) < 3:
            return max(distinct)
        else:
            return sorted(distinct)[-3]

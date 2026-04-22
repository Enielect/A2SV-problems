class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # we can use binary searh to find both the start and the end positions separately
        l, r = 0, len(nums) - 1
        first, second= None, None
        while l <= r:
            m1 = (l + r) // 2
            if nums[m1] == target:
                first = m1
                r = m1 - 1
            elif nums[m1] < target:
                l = m1 + 1
            else:
                r = m1 - 1

        l1, r1 = 0, len(nums) - 1
        while l1 <= r1:
            m1 = (l1+ r1) // 2
            if nums[m1] == target:
                second = m1
                l1 = m1 + 1
            elif nums[m1] < target:
                l1 = m1 + 1
            else:
                r1 = m1 - 1
                
        if first is None:
            return [-1, -1]
        return [first, second]

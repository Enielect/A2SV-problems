class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we just need to implement counting sort(period)
        maximum = max(nums)
        count = [0] * (maximum + 1)

        for num in nums:
            count[num] +=1

        target = 0
        for idx, val in enumerate(count):
            for i in range(val):
                nums[target] = idx
                target +=1

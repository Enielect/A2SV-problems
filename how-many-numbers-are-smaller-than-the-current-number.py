class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_freq = [0] * 101
        res = []
        for num in nums:
            nums_freq[num] +=1
        # generate the prefix sum
        for i in range(1, 101):
            nums_freq[i] += nums_freq[i - 1]
        for num in nums:
            if num == 0:
                res.append(0)
            else:
                res.append(nums_freq[num - 1])
        return res

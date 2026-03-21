class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                triplet_sum = nums[l] + nums[r] + nums[i]
                if triplet_sum == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l + 1]:
                        l +=1
                    while l < r and nums[r] == nums[r - 1]:
                        r -=1
                    l +=1
                    r -=1
                elif triplet_sum > 0:
                    r -=1
                else:
                    l +=1
        return res
            

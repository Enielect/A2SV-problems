class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(target - cur_sum) < abs(target - res):
                    res = cur_sum
                if cur_sum < target:
                    left +=1
                elif cur_sum > target:
                    right -=1
                else:
                    break
        return res

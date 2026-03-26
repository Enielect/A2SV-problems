class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        count = 0
        max_count = 0
        l = 0

        for r in range(n):
            count += nums[r]
            while nums[r] in seen:
                count -= nums[l]
                seen.remove(nums[l])
                l +=1
            seen.add(nums[r])
            max_count = max(max_count, count)
        return max_count

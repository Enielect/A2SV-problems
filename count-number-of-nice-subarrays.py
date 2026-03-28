class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            
            count = 0
            window_sum = 0
            l = 0

            for r in range(len(nums)):
                window_sum += nums[r] % 2
                while window_sum > k:
                    window_sum -= nums[l] % 2
                    l +=1
                count += (r - l + 1)
            return count
        return atMost(k) - atMost(k - 1)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        begin = 0
        seen = set()
        window_sum, max_sum = 0, 0

        for end in range(len(nums)):
            if nums[end] not in seen:
                window_sum += nums[end]
                seen.add(nums[end])

                if end - begin + 1 == k:
                    max_sum = max(max_sum, window_sum)
                    window_sum -= nums[begin]
                    seen.remove(nums[begin])
                    begin +=1
            else:
                while nums[begin] != nums[end]:
                    window_sum -= nums[begin]
                    seen.remove(nums[begin])
                    begin +=1
                begin +=1
        return max_sum

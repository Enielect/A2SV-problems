class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_seen = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[last_seen] = nums[i]
                last_seen +=1
        return last_seen

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # find all elements smaller than this
        # find the total number of this elemts we have seen
        less, count = 0, 0
        for num in nums:
            if num < target:
                less +=1
            if num == target:
                count +=1
        return [less + i for i in range(count)]

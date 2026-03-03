# This was my initial solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if i can get the total number of zeros, and loop through the array that number of times
        # I should be able to perfomr to swaps
        keep = set()
        for i, num in enumerate(nums):
            if num == 0:
                keep.add(i)
        if not keep:
            return

        smallest, steps = min(keep), 0
        while keep:
            for i in range(smallest - steps, len(nums) - 1):
                nums[i+1], nums[i] = nums[i], nums[i+1]
            keep.remove(smallest)
            smallest = min(keep) if keep else 0
            steps +=1
# Made some more research and found this to be more optimal
  class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if i can get the total number of zeros, and loop through the array that number of times
        # I should be able to perfomr to swaps
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
        

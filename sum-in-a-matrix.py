class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # we are going to be looping fro the rows in the matrix
        rows = len(nums)
        cols = len(nums[0])

        max_elements = [0] * cols

        for row in range(rows):
            nums[row].sort(reverse=True)
            for col in range(cols):
                cur = nums[row][col]
                max_elements[col] = max(max_elements[col], cur)

        return sum(max_elements)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse, pse = [n] * n, [-1] * n

        stack1, stack2 = [], []
        max_area = 0

        for i in range(n):
            while stack1 and heights[i] < heights[stack1[-1]]:
                nse[stack1.pop()] = i
            stack1.append(i)

            while stack2 and heights[n - i - 1] < heights[stack2[-1]]:
                pse[stack2.pop()] = n - i - 1
            stack2.append(n - i - 1)

        for i in range(n):
            max_area = max(max_area, heights[i] * (nse[i] - pse[i] - 1))
        return max_area

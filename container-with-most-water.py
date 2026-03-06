class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            lh, rh = height[l], height[r]
            cur_area = (r - l) * min(lh, rh)
            if lh <= rh:
                l +=1
            else:
                r -=1
            max_area = max(max_area, cur_area)
        return max_area

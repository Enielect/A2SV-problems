class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = sorted([x for x,_ in points])
        ans = 0
        for i in range(1, len(points)):
            diff = x_points[i] - x_points[i-1]
            ans = max(ans, diff)
        return ans            

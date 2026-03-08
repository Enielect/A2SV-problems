class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        gr , si = 0, 0
        g.sort()
        s.sort()

        while gr < len(g) and si < len(s):
            if s[si] >= g[gr]:
                ans +=1
                gr +=1
            si +=1
        return ans

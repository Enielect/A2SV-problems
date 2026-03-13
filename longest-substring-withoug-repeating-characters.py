class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen, size = set(), 0
        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l +=1
                l +=1
            else: seen.add(s[r])
            size = max(size, r - l + 1)
            r +=1
        return size

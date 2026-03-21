class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        p_count = Counter(p)
        window_count = Counter(s[:len(p) - 1])
        res = []

        for r in range(len(p) - 1, len(s)):
            window_count[s[r]] +=1
            if p_count == window_count:
                res.append(r - len(p) + 1)
            window_count[s[l]] -=1
            l +=1
        return res

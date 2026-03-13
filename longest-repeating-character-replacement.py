class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l, r = 0, 0
        res, max_count = 0, 0
        while r < len(s):
            counter[s[r]] +=1
            max_count = max(max_count, counter[s[r]])
            if r - l + 1 - max_count > k:
               counter[s[l]] -=1
               l +=1
            res = max(res, r - l + 1)
            r +=1
        return res

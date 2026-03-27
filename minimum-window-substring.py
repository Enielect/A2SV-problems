class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length, count, startIndex = float("inf"), 0, -1
        n = len(s)

        tFreq = Counter(t)

        l = 0
        for r in range(n):
            if tFreq[s[r]] > 0:
                count +=1
            tFreq[s[r]] -=1

            while count == len(t):
                if r - l + 1 < min_length:
                    startIndex = l
                    min_length = r - l + 1

                tFreq[s[l]] +=1
                if tFreq[s[l]] > 0:
                    count -=1
                l +=1
        return s[startIndex: startIndex + min_length] if startIndex != -1 else ""

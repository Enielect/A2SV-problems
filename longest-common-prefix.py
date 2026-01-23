class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        shortest = strs[0]

        n = len(shortest)
        for word in strs[1:]:

            while n >= 0 and shortest:
                if shortest == word[:n]:
                    break
                n -=1
                shortest = shortest[:n]
                
        return shortest

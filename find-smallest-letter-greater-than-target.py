class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = 0, len(letters) - 1
        res = letters[0]
        while l <= h:
            m = (l + h ) // 2
            if letters[m] > target:
                res = letters[m]
                h = m - 1
            else:
                l = m + 1
        return res

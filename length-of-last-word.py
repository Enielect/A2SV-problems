class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word = 0
        for r in range(len(s) - 1, -1, -1):
            if s[r] == ' ':
                break
            word += 1
        return word

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            if s[l] != s[r]:
                left_substring, right_substring = s[l:r], s[l + 1:r + 1]
                return left_substring == left_substring[::-1] or right_substring == right_substring[::-1]
            l, r = l + 1, r - 1
        return True

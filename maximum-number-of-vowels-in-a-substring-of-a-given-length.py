class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = 'aeiou'
        range_cnt = 0
        max_vowel_cnt = 0

        for r in range(k):
            if s[r] in vowels:
                range_cnt +=1
        max_vowel_cnt = range_cnt
        
        l = 0
        for r in range(k, n):
            if s[r] in vowels:
                range_cnt +=1
            if s[l] in vowels:
                range_cnt -=1
            l +=1
            max_vowel_cnt = max(max_vowel_cnt, range_cnt)
        return max_vowel_cnt

## a maybe better solution: This looks cleaner man
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = 'aeiou'
        vowel = 0
        max_vowel = 0

        l = 0
        for r in range(n):
            if s[r] in vowels:
                vowel +=1
            if (r - l + 1) == k:
                max_vowel = max(max_vowel, vowel)
                if s[l] in vowels:
                    vowel -=1
                l +=1
        return max_vowel
